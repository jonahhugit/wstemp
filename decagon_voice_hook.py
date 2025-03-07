# Route for Twilio to handle incoming calls
# <Say> punctuation to improve text-to-speech translation
@router.post("/incoming-call")
def handle_incoming_call(...):
		# POST /conversation/new ... to create a new Decagon conversation
		# https://decagon.notion.site/Chat-API-Endpoints-74e209487aa24a2089f5e2637d8908dc
		conversation_id = requests.post("https://decagon.ai/conversation/new", ...)
		
		# Decagon provides you with a token
		token = ...
		
		# Send a Twilio XML response to connect the call's media stream to Decagon's live voice websocket
    twiml_response = f"""<?xml version="1.0" encoding="UTF-8"?>
                           <Response>
                               <Say>Please wait while we connect your call to the A. I. voice assistant, powered by Twilio and the Open-A.I. Realtime API</Say>
                               <Pause length='1'/>
                               <Say>O.K. you can start talking!</Say>
                               <Connect>
                                  <Stream url='wss://decagon.ai/voice/{conversation_id}?token={token}' />
                              </Connect>
                          </Response>`
    """

    return Response(content=twiml_response, media_type="application/xml")
