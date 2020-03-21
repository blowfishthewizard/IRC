# -*- coding: utf-8 -*-
# developed by acidvegas (https://acid.vegas/weechat)
import re,weechat
def cb_greentext(data,buffer,command):
	if command=='/input return':
		data=weechat.buffer_get_string(buffer,'input')
		if data[0]=='>':data='\x0303'+data
		weechat.buffer_set(buffer,'input',data)
	return weechat.WEECHAT_RC_OK
if weechat.register('greentext','','','','','',''):weechat.hook_command_run('/input return','cb_greentext','')