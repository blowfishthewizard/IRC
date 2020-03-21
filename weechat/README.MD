### Settings
```
/key bind meta-c /bar toggle buflist
/key bind meta-n /bar toggle nicklist
/set buflist.format.buffer						"${if:${type}==server?${if:${window[gui_current_window].buffer.local_variables.server}==${buffer.local_variables.server}?${if:${irc_server.is_connected}?${color:green,235}:${color:lightred,235}}• ${color:default,235}${name}:${if:${irc_server.is_connected}?${color:green,235}:${color:lightred,235}}• ${color:default,235}${indent}${name}}:}${if:${type}=~(channel|private)?${color_hotlist}${indent}${name}:}${if:${type}!~(channel|private|server)?${color:gray}${name}:}"
/set buflist.format.buffer_current				"${if:${type}==server?${if:${window[gui_current_window].buffer.local_variables.server}==${buffer.local_variables.server}?${color:lightred}${if:${irc_server.is_connected}?${color:green,235}:${color:lightred,235}}• ${name}${format_hotlist}:${color:237}${if:${irc_server.is_connected}?${color:green,235}:${color:lightred,235}}• ${name}}${format_lag}${format_hotlist}:${if:${type}=~(channel|private)?• ${name}:${if:${type}!~(channel|private|server)?${color:lightblue}${name}:}}}"
/set buflist.format.hotlist_highlight			"${color:yellow}"
/set buflist.format.hotlist_message				"${color:cyan}"
/set buflist.format.hotlist_private				"${color:yellow}"
/set buflist.look.mouse_wheel					off
/set irc.color.input_nick						default
/set irc.color.nick_prefixes					"y:green;q:green;a:lightred;o:red;h:yellow;v:lightblue;*:lightmagenta"
/set irc.color.reason_quit						darkgray
/set irc.color.topic_new						lightblue
/set irc.ctcp.clientinfo						""
/set irc.ctcp.finger							""
/set irc.ctcp.ping								""
/set irc.ctcp.source							""
/set irc.ctcp.time								""
/set irc.ctcp.userinfo							""
/set irc.ctcp.version							""
/set irc.look.ctcp_time_format					""
/set irc.look.display_ctcp_blocked				off
/set irc.look.display_ctcp_reply				off
/set irc.look.display_ctcp_unknown				off
/set irc.look.display_join_message				""
/set irc.look.display_old_topic					off
/set irc.look.item_nick_modes					off
/set irc.look.join_auto_add_chantype			on
/set irc.look.server_buffer						independent
/set irc.look.smart_filter						off
/set irc.network.ban_mask_default				"*!*@$host"
/set irc.server_default.anti_flood_prio_high	0
/set irc.server_default.anti_flood_prio_low		0 
/set irc.server_default.autorejoin				on
/set irc.server_default.autorejoin_delay		3
/set irc.server_default.capabilities			account-notify,away-notify,cap-notify,multi-prefix,server-time
/set irc.server_default.command_delay			3
/set irc.server_default.msg_part				"G-line: User has been permanently banned from this network."
/set irc.server_default.msg_quit				"G-line: User has been permanently banned from this network."
/set irc.server_default.nicks					"acidvegas,acid_vegas,acidvegas_"
/set irc.server_default.realname				"MOST DANGEROUS MOTHERFUCK"
/set irc.server_default.sasl_mechanism			external
/set irc.server_default.sasl_username			"acidvegas"
/set irc.server_default.ssl_cert				"%h/cert.pem"
/set irc.server_default.ssl_password			"REDACTED"
/set irc.server_default.ssl_verify				off
/set irc.server_default.username				"stillfree"
/set plugins.var.perl.antifuck.autopart			1
/set plugins.var.perl.antifuck.nobufs			1
/set plugins.var.perl.fuckyou.forcejoin			sajoin
/set plugins.var.perl.fuckyou.forcepart			sapart
/set plugins.var.perl.fuckyou.parallel			5
/set plugins.var.perl.highmon.first_run			false
/set plugins.var.perl.highmon.short_names		on
/set plugins.var.perl.keepnick.default_enable	1
/set sec.crypt.hash_algo						sha512
/set weechat.bar.buflist.size_max				20
/set weechat.bar.fset.separator					off
/set weechat.bar.input.color_delim				darkgray
/set weechat.bar.input.conditions				"${window.buffer.full_name} != perl.highmon"
/set weechat.bar.input.items					"[input_prompt]+(away),[input_search],[input_paste],input_text"
/set weechat.bar.input.separator				off
/set weechat.bar.nicklist.size_max				15
/set weechat.bar.status.color_bg				default
/set weechat.bar.status.color_delim				darkgray
/set weechat.bar.status.conditions				"${window.buffer.full_name} != perl.highmon"
/set weechat.bar.status.items					"buffer_name+(buffer_modes)+[buffer_nicklist_count]"
/set weechat.bar.status.separator				off
/set weechat.bar.title.color_bg					black
/set weechat.bar.title.separator				off
/set weechat.bar.title.size_max					2
/set weechat.color.chat_delimiters				darkgray
/set weechat.color.chat_highlight_bg			default
/set weechat.color.chat_host					darkgray
/set weechat.color.chat_nick					white
/set weechat.color.chat_nick_colors				"cyan,magenta,green,brown,lightblue,default,lightcyan,lightmagenta,lightgreen,blue,31,35,38,40,49,63,70,80,92,99,112,126,130,138,142,148,160,162,167,169,174,176,178,184,186,210,212,215,247"
/set weechat.color.chat_prefix_error			lightred
/set weechat.color.chat_prefix_network			lightblue
/set weechat.color.chat_prefix_suffix			darkgray
/set weechat.color.chat_read_marker				darkgray
/set weechat.color.chat_time					235
/set weechat.color.chat_time_delimiters			235
/set weechat.color.separator					darkgray
/set weechat.color.status_name_ssl				white
/set weechat.look.bar_more_down					"▼"
/set weechat.look.bar_more_left					"◀"
/set weechat.look.bar_more_right				"▶"
/set weechat.look.bar_more_up					"▲"
/set weechat.look.buffer_time_format			" %H:%M"
/set weechat.look.confirm_quit					on
/set weechat.look.day_change					off
/set weechat.look.highlight						acidvegas,supernets
/set weechat.look.item_buffer_filter			"•"
/set weechat.look.mouse							on
/set weechat.look.prefix_align_max				15
/set weechat.look.prefix_join					"▬▬▶"
/set weechat.look.prefix_quit					"◀▬▬"
/set weechat.look.prefix_suffix					"│"
/set weechat.look.quote_time_format				"%H:%M"
/set weechat.look.read_marker_string			"─"
/set weechat.look.separator_horizontal			"─"
/set weechat.look.separator_vertical			"│"
/set weechat.look.window_title					"hardchats"
/set weechat.plugin.autoload					"alias,buflist,charset,exec,fset,irc,perl,python,relay,script,trigger"
/set weechat.startup.display_logo				off
/set weechat.startup.display_version			off
```

### Triggers
```
/trigger add hate					modifier	irc_out1_PRIVMSG			"" "/hate/${color:red}${color:underline} HATE ${color:reset}"
/trigger add input_command_color	modifier	"500|input_text_display"	"${tg_string} =~ ^/($|[^/])" "#/(.+)#${color:39}/${color:74}${re:1}#"
/trigger add url_color				modifier	"weechat_print"				"${tg_tags} !~ irc_quit" ";[a-z]+://\S+;${color:32}${color:underline}${re:0}${color:-underline}${color:reset};" ""
```

### Servers
```
/server add blackhat	breaking.technology/6697 -ssl
/server add efnet		efnet.port80.se/6697,irc.choopa.net/6697 -ssl
/server add freenode	irc.freenode.com/6697 -ssl
/server add ircstorm	irc.ircstorm.net/6699 -ssl
/server add oftc		irc.oftc.net/6697 -ssl
/server add sandnet		irc.sandngz.net/6697 -ssl
/server add silph		irc.silph.co/6697 -ssl
/server add supernets	irc.supernets.org/6697 -ssl
/server add unreal		irc.unrealircd.org/6697 -ssl
/server add wtfux		irc.wtfux.org/6697 -ssl

/set irc.server.efnet.autojoin		#2600,#efnetnews,#exchange,#irc30,#lrh
/set irc.server.freenode.autojoin	#archlinux,#ircv3,#music-theory,#python,#raspberrypi,#weechat
/set irc.server.silph.autojoin		#ramen
```

### Services
```
/secure passphrase CHANGEME
/secure set networkname CHANGEME
/set irc.server.networkname.command "/msg NickServ IDENTIFY ${sec.data.networkname}

/msg NickServ register PASSWORD EMAIL
/msg NickServ ACCESS DEL CHANGEME
/msg NickServ ACCESS ADD *@big.dick.acid.vegas
/msg NickServ AJOIN ADD <channel>
/msg NickServ CERT ADD
/msg NickServ SET AUTOOP ON
/msg NickServ SET HIDE EMAIL ON
/msg NickServ SET HIDE STATUS ON
/msg NickServ SET HIDE USERMASK ON
/msg NickServ SET HIDE QUIT ON
/msg NickServ SET KEEPMODES ON
/msg NickServ SET KILL QUICK
/msg NickServ SET PRIVATE ON
/msg NickServ SET SECURE ON
/msg HostServ REQUEST MOST.DANGEROUS.MOTHER.FUCK
/msg HostServ ON
```

### Proxy
```
/proxy add tor socks5 127.0.0.1 9050
/set irc.server.CHANGEME.proxy tor
```

### Relay
```
/secure set relay PASSWORD
/secure set totp SECRET
/set relay.network.max_clients 2
/set relay.network.password ${sec.data.relay}
/set relay.network.totp_secret ${sec.data.totp}
/relay sslcertkey
/relay add ssl.weechat PORT
```
