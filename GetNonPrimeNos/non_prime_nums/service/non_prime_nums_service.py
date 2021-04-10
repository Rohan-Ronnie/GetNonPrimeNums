from tastypie.authorization import Authorization
from tastypie.resources import ALL, ALL_WITH_RELATIONS, Resource
from tastypie.http import HttpAccepted,HttpBadRequest


class GetNonPrimeNumsResource(Resource):
    class Meta:
        authorization = Authorization()

    def dispatch(self, request_type, request, **kwargs):
        if request.method == 'POST':
            try:
                data = self.deserialize(request, request.body,
                                         format=request.META.get('CONTENT_TYPE', 'application/json'))
                if data["app_id"] == "68548109-ce24-4831-8659-2e42d1bcd87f":
                    non_prime_list = []
                    try:
                        if "<class 'int'>" == str(type(data["start_num"])) and "<class 'int'>" == str(type(data["end_num"])):
                            if data["start_num"] < data["end_num"]:
                                start_num = 0
                                if data["start_num"] < 2:
                                    start_num = 2
                                else:
                                    start_num = data["start_num"]

                                for j in range(start_num, data["end_num"]):
                                    if j > 1:
                                        for i in range(2, j):
                                            if (j % i) == 0:
                                                non_prime_list.append(j)
                                                break

                                        else:
                                            pass

                                    else:
                                        pass
                            else:
                                status = "Error"
                                reason = "failed"
                                return self.create_response(request,
                                                            {"status": status, "reason": reason, "response": "end num should be grater than start num",
                                                             'status_code': HttpBadRequest.status_code
                                                             }, HttpBadRequest)
                        else:
                            status = "Error"
                            reason = "failed"
                            return self.create_response(request,
                                                        {"status": status, "reason": reason,
                                                         "response": "end num and start num should be integer",
                                                         'status_code': HttpBadRequest.status_code
                                                         }, HttpBadRequest)
                        status = "success"
                        reason = "working"
                        return self.create_response(request, {"status": status, "reason": reason, "response": non_prime_list,
                                                              'status_code': HttpAccepted.status_code}, HttpAccepted)
                    except Exception as e:
                        status = "Error"
                        reason = "failed"
                        return self.create_response(request, {"status": status, "reason": reason, "response": str(e),
                                                              'status_code': HttpBadRequest.status_code
                                                              }, HttpBadRequest)
                else:
                    status = "success"
                    reason = "working"
                    return self.create_response(request, {"status": status, "reason": reason,
                                                          "response": "please enter valid app id",
                                                          'status_code': HttpAccepted.status_code}, HttpAccepted)
            except Exception as e:
                status = "Error"
                reason = "failed"
                return self.create_response(request, {"status": status, "reason": reason, "response": str(e),
                                                      'status_code': HttpBadRequest.status_code
                                                      }, HttpBadRequest)