  		
			function bubbleSort(array,less) {
				var i=0;
				var j=0;
				function swap(i, j) { var t=array[i]; array[i]=array[j]; array[j]=t }
				for (i=array.length;i>2;i--) {
					for (j=1;j<i-1;j++) {
						if (less(array[j+1],array[j])) {
							swap(j,j+1)
						}
					}
				}
				return array
			}
  			function reload(target) {
  				if (parseInt($(target).attr("count"))<=5) {
  					$(target).attr("src",$(target).attr("src"));
  					$(target).attr("count",parseInt($(target).attr("count"))+1);
  				} else {
  					$(target).attr("onerror","");
  				}
  			}
  			function printf() {
  				//console.log(arguments.callee.caller['result']);
  			}
  			var month_to_number={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
  			
  			function date_wb_to_standard(t) {
  				var s=t.split(" ")
  				var d={}
  				
  				var t=s[3].split(":")
  				d.year=parseInt(s[5])
  				d.month=month_to_number[s[1]]
  				d.day=parseInt(s[2])
  				d.hour=parseInt(t[0])
  				d.minute=parseInt(t[1])
  				d.second=parseInt(t[2])
  				return d
  			}
  			function date_renren_to_standard(t) {
  				var s=t.split(" ")
  				var d={}
  				s1=s[0].split("-")
  				s2=s[1].split(":")
  				d.year=parseInt(s1[0])
  				d.month=parseInt(s1[1])
  				d.day=parseInt(s1[2])
  				d.hour=parseInt(s2[0])
  				d.minute=parseInt(s2[1])
  				d.second=parseInt(s2[2])
  				return d
  			}
  			function printDate(d) {
  				var c=new Date()
  				c.setHours(c.getHours()+c.getTimezoneOffset()/60+8);
  				if ((c.getHours()-d.hour)==0) {
  					return (c.getMinutes()-d.minute)+"分钟以前";
  				}
  				if (((c.getHours()-d.hour)==1)&&((c.getMinutes()-d.minute)<0)) {
  					console.log(c)
  					console.log(d)
  					return (c.getMinutes()-d.minute+60)+"分钟以前";
  				}
  				if ((c.getDate()-d.day)==0) {
  					return (c.getHours()-d.hour)+"小时以前";
  				}
  				if (((c.getDate()-d.day==1))&&((c.getHours()-d.hour<24))) {
  					return (c.getHours()-d.hour+24)+"小时以前";
  				}
  				if ((c.getDate()-d.day)==1) {
  					return "1天以前";
  				}
  				return d.year+"-"+d.month+"-"+d.day+" "+d.hour+":"+d.minute+":"+d.second;
  			}
  			var renren_logo='<img src="/resources/images/icon-renren-19.png" width="16px" height="16px">'
  			var wb_logo='<img src="/resources/images/icon-wb-16.png" width="16px" height="16px">'
  			
  			
  			
  			
  			function wb_handler(v) {
  				var wb_elm=$('<div class="thread"></div>')  					
				var wb_headurl=$('<div class="headurl"></div>')
				wb_headurl.append($('<a target="_blank" target="_blank" href="http://www.weibo.com/'
					+v.user.profile_url+'" ><img count=0 onerror="reload(this)"class="headurl" src="'
					+v.user.profile_image_url+'"></a>'))
				var wb_msgbody=$('<div class="body"></div>')
				wb_msgbody.append($('<a target="_blank" href="http://www.weibo.com/'+v.user.profile_url+'" >'+v.user.name+'</a>'+wb_logo))
				wb_msgbody.append($('<article class="title">'+v.text+'</article>'))
				if (v.retweeted_status!=undefined) {
					wb_msgbody.append($('<article class="status forward">'
					+'<a target="_blank" href="http://www.weibo.com/'+v.retweeted_status.user.profile_url+'">'+v.retweeted_status.user.name+'</a>"&nbsp;'
					+v.retweeted_status.text
					+'<p><a target="_blank" href="'+v.retweeted_status.original_pic+'"><img src="'+v.retweeted_status.thumbnail_pic+'"></a></p>'
					+'<p></p><p class="photo-last-line">'+printDate(date_wb_to_standard(v.retweeted_status.created_at))+'&nbsp;&nbsp;来自'+v.retweeted_status.source+'</p>'
					+'</article>'))
				} else {
					wb_msgbody.append('<a target="_blank" href="'+v.original_pic+'"><img src="'+v.thumbnail_pic+'"></a>')
				}
				wb_msgbody.append('<p class="photo-last-line">'+printDate(date_wb_to_standard(v.created_at))+'&nbsp;&nbsp;来自'+v.source+'</p>')
				//wb_msgbody.append(JSON.stringify(v))
				wb_elm.append(wb_headurl)
				wb_elm.append(wb_msgbody)
				$('div#content').append(wb_elm);
  			}
  			function renren_handler(v) {
  				var renren_elm=$('<div class="thread"></div>')  					
				var renren_headurl=$('<div class="headurl"></div>')
				renren_headurl.append($('<a target="_blank" target="_blank" href="http://www.renren.com/'+v.actor_id+'" ><img count=0 onerror="reload(this)"class="headurl" src="'+v.headurl+'"></a>'))
				var renren_msgbody=$('<div class="body"></div>')
				renren_msgbody.append($('<a target="_blank" href="http://www.renren.com/'+v.actor_id+'" >'+v.name+'</a>'+renren_logo))
				
				switch (v.feed_type) { 
					case 10:	//状态
						renren_elm.addClass("thread10")
						renren_msgbody.append($('<article class="title">'+v.prefix+'</artcle>'))
						if (v.attachment!="") {  // 转发
							renren_msgbody.append($('<article class="status forward"><a target="_blank" href="http://www.renren.com/'+v.attachment[0].owner_id+'">'+v.attachment[0].owner_name+'</a>&nbsp;:&nbsp;'+v.attachment[0].content+'</article>'));
						}
						break;
					case 30:   //照片
						renren_elm.addClass("thread30")
						if (v.attachment[0].content==undefined) {
							renren_msgbody.append($('<article class="title">&nbsp;'+v.prefix+'&nbsp;至&nbsp;<a target="_blank" href="'+v.href+'">'+v.title+'</a></artcle>'))
						} else {
							renren_msgbody.append($('<article class="title">'+v.attachment[0].content+'</artcle>'))
						}
						renren_msgbody.append('<a target="_blank" href="'+v.attachment[0].href+'"><img count=0 onerror="reload(this)"style="max-height:220px;" src="'+v.attachment[0].raw_src+'"></a>');
								
						break;
					case 32: //照片分享
						renren_elm.addClass("thread32")
						if (v.trace=="") {
							renren_msgbody.append($('<article class="title">'+v.prefix+'</artcle>'))
						} else {
							var trace = v.trace.text;
							for (i in v.trace.node) {
								trace=trace.replace(v.trace.node[i].name,'<a target="_blank" href="http://www.renren.com/'+v.trace.node[i].id+'">'+v.trace.node[i].name+'</a>');
							}
							renren_msgbody.append($('<article class="title">'+trace+'</artcle>'))
						}
						renren_msgbody.append('<article class="status forward"><a target="_blank" href="'
						+v.attachment[0].href
						+'"><img count=0 onerror="reload(this)"style="max-height:220px;" src="'
						+v.attachment[0].raw_src
						+'"></a><p class="last-line" style="margin-top:10px;" >'+v.description+'</p><p class="photo-last-line">所属&nbsp;:&nbsp;'
						+'<a target="_blank" href="'+v.href+'">'+v.title+'</a>'
						+'</p><span style="float:right;display:inline;color:#000;">来自&nbsp;:&nbsp;<a target="_blank" href="http://www.renren.com/'+v.attachment[0].owner_id
						+'">'+v.attachment[0].owner_name+'</a></span></article>');
						
						break;
					case 50: //视频分享
						renren_elm.addClass("thread50");
						if (v.message=="") {
							renren_msgbody.append($('<article class="title">'+v.prefix+'</artcle>'))
						} else {
							renren_msgbody.append($('<article class="title">'+v.message+'</artcle>'))
						}
						renren_msgbody.append('<article class="status forward">'
						+'<div class="video"><a target="_blank" href="'+v.attachment[0].href+'"><img src="'+v.attachment[0].src+'"></a></div>'
						+'<div class="video-description"><a target="_blank" href="'+v.attachment[0].href+'">'
						+v.title+'</a>'
						+'<p class="video-last-line">来自：&nbsp;'
						+'<a target="_blank" style="color:#000;" href="http://www.renren.com/'+v.attachment[0].owner_id+'">'+v.attachment[0].owner_name+'</a>'
						+'</p>'
						+'</div>'
						+'</article>');
						break;
					case 21: //日志分享
						renren_elm.addClass("thread21")
						if (v.trace==undefined) {
							renren_msgbody.append($('<article class="title">'+v.prefix+'</artcle>'))
						} else {
							var trace = v.trace.text;
							for (i in v.trace.node) {
								trace=trace.replace(v.trace.node[i].name,'<a target="_blank" href="http://www.renren.com/'+v.trace.node[i].id+'">'+v.trace.node[i].name+'</a>');
							}
							renren_msgbody.append($('<article class="title">'+trace+'</artcle>'))
						}
						
						renren_msgbody.append('<article class="status forward"><p><a target="_blank" href="'+v.href+'">'+v.title+'</a></p><p>'
												+v.description+'</p><p class="photo-last-line">'
												+'来自:&nbsp;<a target="_blank" href="http://www.renren.com/'+v.attachment[0].owner_id+'">'
												+v.attachment[0].owner_name
												+'</a></p></article>')
							
						
						break;
					case 23: //公共主页分享日志
						renren_elm.addClass("thread23")
						if (v.trace==undefined) {
							renren_msgbody.append($('<article class="title">'+v.prefix+'</artcle>'))
						} else {
							var trace = v.trace.text;
							for (i in v.trace.node) {
								trace=trace.replace(v.trace.node[i].name,'<a target="_blank" href="http://www.renren.com/'+v.trace.node[i].id+'">'+v.trace.node[i].name+'</a>');
							}
							renren_msgbody.append($('<article class="title">'+trace+'</artcle>'))
						}
						renren_msgbody.append('<article class="status forward"><p><a target="_blank" href="'+v.href+'">'+v.title+'</a></p><p>'
												+v.description+'</p><p class="photo-last-line">'
												+'来自:&nbsp;<a target="_blank" href="http://www.renren.com/'+v.attachment[0].owner_id+'">'
												+v.attachment[0].owner_name
												+'</a></p></article>')
							
						break;
				}
				if (v.source !=undefined) {
					renren_msgbody.append($('<p class="last-line">'+printDate(date_renren_to_standard(v.update_time))+'&nbsp;<a target="_blank" href="'+v.source.href+'">通过'+v.source.text+'发表</a></p>'));
				} else {
					renren_msgbody.append($('<p class="last-line">'+printDate(date_renren_to_standard(v.update_time))+'</p>'));
				}
				renren_elm.append(renren_headurl)
				renren_elm.append(renren_msgbody)
				$('div#content').append(renren_elm);
			}
  			