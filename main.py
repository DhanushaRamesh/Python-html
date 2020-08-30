f=open("test.html","r")
data=f.read()
f.close()

#SERVER SIDE PROCESSING START (using Python at Server end)

data=data.replace("PLACEHOLDER_001","Newly added data 1")    # All this replace values should be unique in html page so it replaces exactly at that place
data=data.replace("PLACEHOLDER_002","Newly added data 2")
data=data.replace("DISP_SUCCESS_1","none")
data=data.replace("DISP_FAIL_2","none")
data=data.replace("DISP_SUCCESS_2","")
data=data.replace("green","red")


#SERVER SIDE PROCESSING END 



#CLIENT SIDE PROCESSING START (using Client PC using javascript)

head="""
<head>
<style>
cache
{
	display:none;
}
#e::before
{
	content:"NEW DATA 1";
}
#f::before
{
	content:"NEW DATA 2";
}
</style>
</head>
"""

dictionary="""
<cache>
{"#a":"style=background-color:red;",
"#b":"style=color:red;",
"#c":"style=font-weight:bold;",
"#d":"style=background-color:red;",
".a":"style=background-color:teal;"
}
</cache>
"""
dictionary=dictionary.replace("\n","")
data=data.replace("<cache></cache>",dictionary)

cbody="""
<script>
document.body.onload = function(){
var data=document.getElementsByTagName("cache")[0].firstChild.textContent;
var json_data=JSON.parse(data);
var x,y;
for (x in json_data)
{
	var part=json_data[x].split("=")[0];
	var val=json_data[x].replace(part+"=","")
	if(document.querySelectorAll(x).length === 1)
	{
		document.querySelector(x).setAttribute(json_data[x].split("=")[0],val);
	}
	else if(document.querySelectorAll(x).length > 1)
	{
		for (var y=0;y<document.querySelectorAll(".a").length;y++)
		{
			document.querySelectorAll(".a")[y].setAttribute(json_data[x].split("=")[0],val);
		}
	}
}
}
</script>
</body>
"""


data=data.replace("<head></head>",head)
data=data.replace("</body>",cbody)

#CLIENT SIDE PROCESSING END

f=open("output.html","w+")
f.write(data)
f.close()

	
