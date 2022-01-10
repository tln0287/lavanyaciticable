$(document).ready(function(){
	
	$('docs-date').on('changeDate', function(ev){
		$(this).datepicker('hide');
	});
	$('#myscreen').height($(document).height() - 135);
});
function getMenuDit(mid,links){
	
	$.ajax({
		url : site_url + 'logfile/getMenuDit/',
		type: "GET",        
		dataType: "html",
		data:{mid:mid,links:links},
		success: function(data)
		{
			window.location.href =  site_url + links;
		}
		
	});
}
function formatDecimal(x) {
    return parseFloat(parseFloat(x).toFixed(2));
}
function formatMoney(x) {
    
    return x.toFixed(2);
    
}
function formatDate(date) {
     var d = new Date(date),
         month = '' + (d.getMonth() + 1),
         day = '' + d.getDate(),
         year = d.getFullYear();

     if (month.length < 2) month = '0' + month;
     if (day.length < 2) day = '0' + day;

     return [day, month , year].join('-');
	 
	 
 }
 function getCurrentDate() {
     var d = new Date();
         month = '' + (d.getMonth() + 1),
         day = '' + d.getDate(),
         year = d.getFullYear();

     if (month.length < 2) month = '0' + month;
     if (day.length < 2) day = '0' + day;

     return [day, month , year].join('-');
	 
	 
 }

function simpleArray(target){
    var arr = [];
    $.each(target, function(i, e){
        $.each(e, function(key, val){
            arr.push(key);
            arr.push(val);
        });
    });
    return arr;
}

function upperCaseF(a){
	setTimeout(function(){
		a.value = a.value.toUpperCase();
	}, 1);
}
function lowercaseF(a){
	setTimeout(function(){
		a.value = a.value.toLowerCase();
	}, 1);
}
function validate(event) {
 
  var controlKeys = [8, 9, 13, 37, 39, 46];
  var isControlKey = controlKeys.join(",").match(new RegExp(event.which));
  if (!event.which || (48 <= event.which && event.which <= 57) || isControlKey) {
	return;
  } else {
	event.preventDefault();
  }
}
function validate1(event) {
 
  var controlKeys = [8];
  var isControlKey = controlKeys.join(",").match(new RegExp(event.which));
  if (!event.which || (48 <= event.which && event.which <= 57) || isControlKey) {
	return;
  } else {
	event.preventDefault();
  }
}
function validateTime(event) {
 
  var controlKeys = [58];
  var isControlKey = controlKeys.join(",").match(new RegExp(event.which));
  if (!event.which || (48 <= event.which && event.which <= 57) || isControlKey) {
	return;
  } else {
	event.preventDefault();
  }
}
function parseHM(obj) {
    
	var src = $(obj).val();
	if(src.length==2){
		$(obj).val(src+':');
	}		
}
function parseDMY(obj) {
    
	var src = $(obj).val();
	if(src.length==2){
		$(obj).val(src+'-');
	}	
	if(src.length==5){
		$(obj).val(src+'-');
	}
	
}
function validateSpNum(obj){		
	var yourInput = $(obj).val();
	re = /[`~!@#$%^&*(0-9)_|+\-=?;:'",.<>\{\}\[\]\\\/]/gi;
	var isSplChar = re.test(yourInput);
	if(isSplChar)
	{
		var no_spl_char = yourInput.replace(/[`~!@#$%^&*(0-9)_|+\-=?;:'",.<>\{\}\[\]\\\/]/gi, '');
		$(obj).val(no_spl_char);
	}
}
function validateText(obj){		
	var yourInput = $(obj).val();
	re = /[`~!@#$%^&*()_|+\-=?;:'",.<>\{\}\[\]\\\/]/gi;
	var isSplChar = re.test(yourInput);
	if(isSplChar)
	{
		var no_spl_char = yourInput.replace(/[`~!@#$%^&*()_|+\-=?;:'",.<>\{\}\[\]\\\/]/gi, '');
		$(obj).val(no_spl_char);
	}
}
function isValidEmailAddress(emailAddress) {
	if(emailAddress){
		var pattern = /^([a-z\d!#$%&'*+\-\/=?^_`{|}~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+(\.[a-z\d!#$%&'*+\-\/=?^_`{|}~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+)*|"((([ \t]*\r\n)?[ \t]+)?([\x01-\x08\x0b\x0c\x0e-\x1f\x7f\x21\x23-\x5b\x5d-\x7e\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|\\[\x01-\x09\x0b\x0c\x0d-\x7f\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))*(([ \t]*\r\n)?[ \t]+)?")@(([a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|[a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF][a-z\d\-._~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]*[a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])\.)+([a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|[a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF][a-z\d\-._~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]*[a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])\.?$/i;
		if(pattern.test(emailAddress)){
			
		}else{
			alert("invalid email");
			$('#email').val('');
		}
	}
	
	
};
function genBarCode(){		
	
	$.ajax({
		type: "get", async: false,
		url: site_url + "products/getBarCodeGenerate",
		dataType: "html",				
		success: function (data) {
		
			$('#code').val(data);
		}
	});		
}
function toggleMenu(){
	
	$(".todo-sidebar").toggle("slow", function(){
		if($(".todo-sidebar").is(":visible")){
			
		} else{
			
		}

	});
	
}
function nameonly(evt) {
    var theEvent = evt || window.event;
    var key = theEvent.keyCode || theEvent.which;
    key = String.fromCharCode(key);
    if (key.length == 0) return;
    var regex = /^[a-zA-Z. \b\t]/;
    if (!regex.test(key)) {
	    theEvent.returnValue = false;
	if (theEvent.preventDefault) theEvent.preventDefault();
	}
}

function noonly(evt) {
    var theEvent = evt || window.event;
    var key = theEvent.keyCode || theEvent.which;
    key = String.fromCharCode(key);
    if (key.length == 0) return;
    var regex = /^[0-9\b\t]/;
    if (!regex.test(key)) {
	    theEvent.returnValue = false;
	if (theEvent.preventDefault) theEvent.preventDefault();
	}
}

function emailonly(evt) {
    var theEvent = evt || window.event;
    var key = theEvent.keyCode || theEvent.which;var key1 = theEvent.keyCode || theEvent.which;
    key = String.fromCharCode(key);
    if (key.length == 0) return;
    var regex = /^[a-zA-Z0-9._@\b\t]/;
    if (!regex.test(key) && key1!=37 && key1!=39) { 
	    theEvent.returnValue = false;
	if (theEvent.preventDefault) theEvent.preventDefault();
	}
}


function getTumbs(uploadclassImgs,imgview){
	
	var img =  document.getElementById(uploadclassImgs).value;
	if(img==''){
		
	}else{
		
		input = document.getElementById(uploadclassImgs);
		filess = input.files[0];
		var fsize = filess.size;			
		var type = (/[.]/.exec(img)) ? /[^.]+$/.exec(img) : undefined;	
			
			
			if((type=='jpg') || (type == 'png') || (type == 'jpeg') || (type == 'JPG')){
		
			}else{
				alert("Sorry! Please Select Image only");
				return false;				
			}
			
			if(fsize>5000000){
				alert("Sorry! Please Select Below 420Mb Files");
				return false;
			}
		
	
		var input, filess;
		input = document.getElementById(uploadclassImgs);
		filess = input.files[0];
		var reader = new FileReader();
		reader.onload = function (e) {
			$('#'+imgview).attr('src', e.target.result);
			var btn = '<div style="border-bottom-left-radius:3px;border-bottom-right-radius:3px;position: relative;text-align:center;margin-top:-56px;margin-left:10px;margin-right:6px;background:#9d9d9d;padding:6px;opacity: 0.7;filter: alpha(opacity=70);border:1px solid #9d9d9d;">';
				btn += '<span class="test1" style="color:#770000;font-weight:bold;" >Remove</span>';
				btn += '</div>';
			$('#remove_btn').html(btn);
		}

			reader.readAsDataURL(input.files[0]);
	}
}
