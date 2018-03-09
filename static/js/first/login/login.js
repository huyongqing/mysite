var app  = new Vue({
		el : '#app',
		data : {
			name : 'yongqing.hu',
			password : 'HYq23931582!'
		},
		methods : {
			check : function(event){
				//获取值
				var name = this.name;
				var password = this.password;
				alert(this.name)
				if(name == '' || password == ''){
					this.$message({
						message : '账号或密码为空！',
						type : 'error'
					});
					return;
				}
				alert("----"+this.name)
				$.ajax({
					url : '/check/',
					type : 'post',
					data : {
						name : name,
						password : password
					},
					success : function(data) {
						var result = data.result;


						if(result == 'true' || result == true){
							alert("登录成功");
							 window.location.href = '/index/';
						}else {
							alert("登录失败");
						}
					},
					error : function(data) {

						alert("输出异常了胡永青");
					},
					dataType : 'json',
				})
			}
		}
	});