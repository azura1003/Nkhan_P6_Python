import psutil
import win32serviceutil

def getService(Audiosrv):
    service = None
    try:
        service = psutil.win_service_get(Audiosrv)
        service = service.as_dict()
    except Exception as ex:
        print (str(ex))

    return service

service = getService('Audiosrv')

#print(service)

if service:
        print ("service found")
else:
        print ("service not found")

if service and service['status'] == 'running':

        print ("service is running")
else:

         print ("service is not running")
         service = "Audiosrv"
         win32serviceutil.StartService(service)