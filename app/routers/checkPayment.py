from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import PlainTextResponse, JSONResponse
import logging
import httpx
import json

router = APIRouter()

# Your Supabase URL and API key
SUPABASE_URL = "https://zmvjylvafmgqpxqtrblc.supabase.co"
SUPABASE_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inptdmp5bHZhZm1ncXB4cXRyYmxjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjM0ODk4MTIsImV4cCI6MjAzOTA2NTgxMn0.-qK5cu9zPoVtcpGAf14-XuJ55SMYXpfpXXgp6lz-Z4M"
SUPABASE_RPC_URL = f"{SUPABASE_URL}/rest/v1/rpc/insert_payu_webhook_response"

@router.post("/payu/webhook", response_class=PlainTextResponse)
async def payu_webhook(request: Request):
    # Read raw form data from the request body
    form_data = await request.form()
    data_dict = dict(form_data)

    # Optional: Log the received data for verification
    logging.info("Received PayU Webhook: %s", data_dict)
    
    # Prepare data to be sent to Supabase API (RPC function)
    payload = {
        "_addedon": data_dict.get("addedon"),
        "_address1": data_dict.get("address1"),
        "_address2": data_dict.get("address2"),
        "_amount": data_dict.get("amount"),
        "_bank_ref_no": data_dict.get("bank_ref_no"),
        "_bank_ref_num": data_dict.get("bank_ref_num"),
        "_bankcode": data_dict.get("bankcode"),
        "_card_no": data_dict.get("card_no"),
        "_card_token": data_dict.get("card_token"),
        "_city": data_dict.get("city"),
        "_country": data_dict.get("country"),
        "_curl": data_dict.get("curl"),
        "_discount": data_dict.get("discount"),
        "_email": data_dict.get("email"),
        "_error": data_dict.get("error"),
        "_error_message": data_dict.get("error_message"),
        "_field0": data_dict.get("field0"),
        "_field1": data_dict.get("field1"),
        "_field2": data_dict.get("field2"),
        "_field3": data_dict.get("field3"),
        "_field4": data_dict.get("field4"),
        "_field5": data_dict.get("field5"),
        "_field6": data_dict.get("field6"),
        "_field7": data_dict.get("field7"),
        "_field8": data_dict.get("field8"),
        "_field9": data_dict.get("field9"),
        "_firstname": data_dict.get("firstname"),
        "_furl": data_dict.get("furl"),
        "_hash": data_dict.get("hash"),
        "_key": data_dict.get("key"),
        "_lastname": data_dict.get("lastname"),
        "_mecode": data_dict.get("meCode"),
        "_mihpayid": data_dict.get("mihpayid"),
        "_mode": data_dict.get("mode"),
        "_net_amount_debit": data_dict.get("net_amount_debit"),
        "_offer_availed": data_dict.get("offer_availed"),
        "_offer_key": data_dict.get("offer_key"),
        "_payment_source": data_dict.get("payment_source"),
        "_pg_type": data_dict.get("pg_type"),
        "_phone": data_dict.get("phone"),
        "_productinfo": data_dict.get("productinfo"),
        "_state": data_dict.get("state"),
        "_status": data_dict.get("status"),
        "_surl": data_dict.get("surl"),
        "_txnid": data_dict.get("txnid"),
        "_udf1": data_dict.get("udf1"),
        "_udf10": data_dict.get("udf10"),
        "_udf2": data_dict.get("udf2"),
        "_udf3": data_dict.get("udf3"),
        "_udf4": data_dict.get("udf4"),
        "_udf5": data_dict.get("udf5"),
        "_udf6": data_dict.get("udf6"),
        "_udf7": data_dict.get("udf7"),
        "_udf8": data_dict.get("udf8"),
        "_udf9": data_dict.get("udf9"),
        "_unmappedstatus": data_dict.get("unmappedstatus"),
        "_zipcode": data_dict.get("zipcode"),
    }

    # Send data to Supabase RPC function
    async with httpx.AsyncClient() as client:
        response = await client.post(
            SUPABASE_RPC_URL,
            json=payload,
            headers={
                "Content-Type": "application/json",
                "apikey": SUPABASE_API_KEY,
                "Authorization": f"Bearer {SUPABASE_API_KEY}",
            },
        )
    response_data=response.json()
    if response_data['success_code'] == 101:
        # Check if the Supabase function successfully processed the data
        logging.info("Successfully inserted PayU webhook response into Supabase")
        return JSONResponse(content={"message": "Success", "code": 101}, status_code=200)
    else:
        # Handle errors if the response from Supabase is not successful
        logging.error(f"Failed to insert data into Supabase: {response.text}")
        return f"Error: {response.text}"

