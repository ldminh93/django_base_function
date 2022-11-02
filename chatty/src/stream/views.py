# from django.shortcuts import render
# from django.http import StreamingHttpResponse
# from stream.camera import LiveWebCam
#
#
# def stream(request):
#     return render(request, 'live_stream.html')
#
#
# def gen(camera):
#     while True:
#         frame = camera.get_frame()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
#
#
# def mask_stream(request):
#     return StreamingHttpResponse(gen(LiveWebCam()), content_type='multipart/x-mixed-replace;boundary=frame')
#
# #
# # def video_feed(request):
# # 	return StreamingHttpResponse(gen(VideoCamera()),
# # 					content_type='multipart/x-mixed-replace; boundary=frame')
# #
# #
# # def webcam_feed(request):
# # 	return StreamingHttpResponse(gen(IPWebCam()),
# # 					content_type='multipart/x-mixed-replace; boundary=frame')
# #
# #
# # def mask_feed(request):
# # 	return StreamingHttpResponse(gen(MaskDetect()),
# # 					content_type='multipart/x-mixed-replace; boundary=frame')
# #