from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
import requests,json

# Create your views here.
# 创建一个视图函数
def index(request):
    # 在视图函数中进行响应
    return render(request,'index.html')

 
def get_img(request,aid):
	# 确定基准地址
	base_url = 'https://api.bilibili.com/x/web-interface/view?aid={}'.format(aid)

	# 构建请求头
	headers = {
		'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36',
		'Referer': 'https://www.bilibili.com/video/av{}'.format(aid)
	}
	# 获取页面返回结果
	req = requests.get(base_url,headers=headers)

	# 利用json进行解析
	json_html = json.loads(req.text)

	# 获取状态码
	status  = json_html['code']

	# 判断是否存在
	if str(status) == '-404':
		return '啥也木有,请检查AV号是否填写错误'

	# 获取图片nurl
	img_url = json_html['data']['pic']

	return img_url




def bili_index(request):
	context = {'info':'开始获取吧~','status':'success'}
	return render(request,'bilibili.html',context)
	
def bili_get(request):
	# 从post中获取av号
	aid = request.POST.get('aid')
	print(aid)
	try:
		res = get_img(request,aid)
		# 分配数据
		context = {'imgurl':res,'status':'success','info':'获取成功'}
		return JsonResponse(context)
	except :
		# 分配数据
		context = {'info':'啥也木有,请检查AV号是否填写错误!','status':'error','imgurl':''}
		return JsonResponse(context)

		
        

        