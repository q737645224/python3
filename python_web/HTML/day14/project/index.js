window.onload = function (){
	/*-----------�����˵�---------*/

	//1. ��ȡԪ�ؽڵ�
	var currentAddr = document.getElementsByClassName('currentAddress')[0];
	var select = document.getElementsByClassName('select')[0];
	
	//��ȡ�ڲ��б��е�ַ��
	var address = select.children;
	//Ϊÿһ����ӵ���¼�
	for(var i = 0; i < address.length; i ++){
		address[i].onclick = function(){
			//��ֵ
			currentAddr.innerHTML = this.innerHTML;
		};
	}

	/*-----------ͼƬ�ֲ�-----------*/
	//1. ��ȡͼƬ����
	//2. ��ʱ��ʵ��ͼƬ�л�
	//3. ͼƬ�л���Ҫ�л������±꣬��ֹ����Խ��

	var banner = document.getElementsByClassName('wrapper')[0];
	var imgs = banner.children; //ͼƬ����
	var imgNav = document.getElementsByClassName('imgNav')[0];
	var indInfo = imgNav.children; //��������
	var imgIndex = 0; //��ʼ�±�
	var timer;
	timer = setInterval(autoPlay,1000); //��ʱ��
	function autoPlay(){
		//����Ԫ����������ʾ
		imgs[imgIndex].style.display = "none";
		/*
		++ imgIndex;
		if(imgIndex == imgs.length){
			imgIndex = 0;
		}
		*/
		imgIndex = ++ imgIndex == imgs.length ? 0 : imgIndex;

		imgs[imgIndex].style.display = "block";

		for(var i = 0; i < indInfo.length; i ++){
			indInfo[i].style.background = "gray";
		}
		//�л����� �л�����ɫ
		indInfo[imgIndex].style.background = "red";
	}
	banner.onmouseover = function (){
		//ֹͣ��ʱ��
		clearInterval(timer);
	};

	banner.onmouseout = function (){
		timer = setInterval(autoPlay,1000);
	};

};