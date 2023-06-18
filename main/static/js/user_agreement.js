body{
	background: #2c2c2c;
	header:100%;
}
*{
	margin: 0;
	padding: 0;
}
.header{
	background: #181818;
	height: 70px;
	width: 100%;
	display: flex;
}
.Logo,.Top_menu{
display: inline-block;
margin-right:35px ;
}
.Logo{
	vertical-align: middle;
}
.Logo img{
max-height: 70px;
padding-left:500px;
}
.Top_menu li{
	display: inline-block;
	vertical-align: middle;
	margin-right:25px;
}
.Top_menu{
	padding-left: 20px;
}
.Top_menu a{
	vertical-align: middle;
	color: #ffffff;
	font-size: 24px;
	font-family: arial;
}
.Top_menu a:hover{
	vertical-align: middle;
	color: #eb5959;
	font-size: 24px;
	font-family: arial;
}
a{
	text-decoration: none;
}
.footer{
	background: #181818;
	height: 250px;
	width: 100%;
}
.main{
	min-height: calc(100vh - 320px);
}
.link_footer li{
	display: inline-block;
	vertical-align: middle;
}
.block_footer{
	padding-left:500px;
}
.text_link_footer{
	padding-top: 50px;
	padding-bottom: 10px;
	font-size: 24px;
	font-family: arial;
	color:#fff;
}
.link_footer{
	float: left;
	padding-right: 50px;
}
.info_footer ul{
	padding-top: 50px;
}
.info_footer li{
	padding-bottom:15px;
	
}
.footer img{
	max-width:40px; /* you can use % */
   height: auto;
   color:#fff;
}
.info_footer a,p{
	font-size: 22px;
	color:#aaa;
}
.info_footer a:hover{
	font-size: 22px;
	color:#fff;
}
li{
	list-style-type: none;
}