from fastapi import (
    APIRouter,
)
import os
from .schemas import RisRequest
from amocrm.v2 import Lead, Contact

from ..config import token_initialization


ris_integration_router = APIRouter(
    prefix='/ris-integration',
    tags=['RIS интеграция']
)


@ris_integration_router.get("/ping")
async def ris_ping_pong():
    return "pong"


@ris_integration_router.post(
    "/create-deal/product/get-order",
)
async def ris_create_deal_product(
    order_data: RisRequest
):
    tokens = await token_initialization()
    pipeline_id = int(os.environ.get('ris_product_pipeline_id'))
    status = False
    contact_data = {
        "name": order_data.name,
        "custom_fields_values": [
            {
                "field_code": "PHONE",
                "values": [
                    {
                        "value": order_data.phone if order_data.phone else ""
                    }
                ]
            },
            {
                "field_code": "EMAIL",
                "values": [
                    {
                        "value": order_data.email if order_data.email else ""
                    }
                ]
            }
        ]
    }
    new_contact = Contact.objects.create(contact_data)
    new_contact_id = new_contact.id

    lead_data = {
        'name': f"Заявка на курс от {order_data.campaign_id}",
        'pipeline_id': pipeline_id,
        "_embedded": {
            "contacts": [
                {
                    "id": new_contact_id,
                },
            ],
        },
        "custom_fields_values": [
            {
                "field_code": "UTM_CAMPAIGN",
                "values": [
                    {
                        "value": order_data.campaign_id if order_data.campaign_id else ""
                    }
                ]
            },
            {
                "field_code": "UTM_SOURCE",
                "values": [
                    {
                        "value": "RisPromo"
                    }
                ]
            },
            {
                "field_id": 666391,
                "values": [
                    {
                        "value": "RisPromo"
                    }
                ]
            }
        ]
    }

    new_lead = Lead.objects.create(lead_data)

    if isinstance(new_lead.id, int):
        status = True

    return {
        "success": status,
        "data": order_data.model_dump()
    }
