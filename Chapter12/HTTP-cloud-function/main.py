from datetime import date, datetime

def today_datatime(request):

  request_json = request.get_json()
  if request.args and 'requester' in request.args:
    requster_name = request.args.get('requester')
  elif request_json and 'requester' in request_json:
    requster_name = request_json['requester']
  else:
    requster_name = f'anonymous'

  today = date.today()
  now = datetime.now()
  resp = "{date:" + today.strftime("%B %d, %Y") + \
      ", time: " + now.strftime("%H:%M:%S") + '}'
  return f'Hello ' + requster_name + "! Here is today date and time:\n" + resp
