from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content

def handle_storage_event(event, context):

  from_email = Email("masif.72@gmail.com")
  to_emails = To("masif.carleton@gmail.com")
  subject = "Your Storage Bucket Notification"
  content = Content("text/plain",
                    f"Bucket Impacted:{event['bucket']} \n" +
                    f"File Impacted: {event['name']} \n " +
                    f"Event Time: {event['timeCreated']} \n" +
                    f"Event ID: {context.event_id} \n" +
                    f"Event Type: {context.event_type}"
                    )
  mail = Mail(from_email, to_emails, subject, content)
  mail_json = mail.get()

  sg = SendGridAPIClient()
  response = sg.client.mail.send.post(request_body=mail_json)
  print(response.status_code) # for logging purpose
  print(response.headers)
