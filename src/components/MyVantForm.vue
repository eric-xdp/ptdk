<template>
  <div class="formDiv">
    <van-form @submit="onSubmit">
      <!-- 班级 -->
    <div id="alwaysShow">
    <van-field readonly clickable placeholder="请选择班级" label="班级" colon :value="classValue" 
    @click="($event) => {fieldClick($event, 'showClass')}"/>
    <van-popup v-model="showClass" position="bottom" get-container="formDiv" @click="($event) => {getMyValue($event,'showClass')}">
            <van-picker title="班级" visible-item-count="10" :default-index="defaultIndex" :columns="classColumns"
             @change="valueChange" ref ="classPicker"/>
    </van-popup>

    <!-- 姓名 -->
    <!-- <van-field v-model="name" label="法名" colon placeholder="请输入用户名" /> -->
     <van-field readonly clickable :value="name" label="法名" colon placeholder="请选择法名" @click="($event) => {fieldClick($event, 'showName')}"/>
    <van-popup v-model="showName" round position="bottom" @click="($event) => {getMyValue($event,'showName')}">
      <van-picker visible-item-count="10"  title="法名" :columns="nameColumns"
       @change="valueChange" ref ="namePicker"/>
    </van-popup>
    <!-- 日期 -->
    <van-field readonly clickable placeholder="请选择日期" label="考核日期" :value="date" colon @click="isDate" />
    <van-calendar v-model="show" :show-confirm="false" :max-date="maxDate" :min-date="minDate" @confirm="setMyDate" @open="onOpen"/>
    <!-- 定课 -->
    <van-field readonly clickable :value="dingke" label="定课" colon placeholder="请选择定课遍数" @click="($event) => {fieldClick($event, 'showDingke')}"/>
    <van-popup v-model="showDingke" round position="bottom" @click="($event) => {getMyValue($event,'showDingke')}">
      <van-picker  visible-item-count="10" :default-index="defaultIndex" title="定课遍数" option="dingke" :columns="dingkeColumns" 
      @change="valueChange" ref ="dingkePicker"/>
    </van-popup>
    <!-- 闻思 -->
    <!-- <van-field v-model="wensi" label="闻思" colon placeholder="请输入闻思时间（分钟）" type="digit"/> -->
    <van-field readonly clickable :value="wensi" label="闻思" colon placeholder="请选择闻思时间（分钟）" @click="($event) => {fieldClick($event, 'showWensi')}"/>
    <van-popup v-model="showWensi" round position="bottom" @click="($event) => {getMyValue($event,'showWensi')}">
      <van-picker visible-item-count="10" :default-index="defaultIndex" title="闻思时间" :columns="wensiColumns"  
       @change="valueChange" ref="wensiPicker"/>
    </van-popup>
    
    <!-- 原文朗诵 -->
    <!-- <van-field v-model="langsong" label="原文朗诵" colon placeholder="请输入原文朗诵遍数" type="digit"/> -->
    <van-field readonly clickable :value="langsong" label="原文诵读" colon placeholder="请选择原文诵读遍数" @click="($event) => {fieldClick($event, 'showLangsong')}" />
    <van-popup v-model="showLangsong" round position="bottom" @click="($event) => {getMyValue($event,'showLangsong')}">
      <van-picker visible-item-count="7" :default-index="defaultIndex" title="诵读遍数" :columns="langsongColumns"  
       @change="valueChange" ref ="langsongPicker"/>
    </van-popup>

    <!-- 菩提导航打卡 -->
    <!-- <van-field v-model="daka" label="菩提导航" colon placeholder="请输入菩提导航打卡遍数" type="digit"/> -->
    <van-field readonly clickable :value="daka" label="菩提导航" colon placeholder="请选择菩提导航打卡遍数" @click="($event) => {fieldClick($event, 'showDaka')}"/>
    <van-popup v-model="showDaka" round position="bottom" @click="($event) => {getMyValue($event,'showDaka')}">
      <van-picker visible-item-count="10" :default-index="defaultIndex" title="打卡遍数" :columns="dakaColumns"  
       @change="valueChange" ref ="dakaPicker"/>
    </van-popup>
    <!-- 一日一转 -->
    <van-field readonly clickable placeholder="一日一转了吗？" colon label="一日一转" :value="yiri" @click="showBoolean = true" />
    <van-action-sheet v-model="showBoolean" :actions="actions" @select="onSelect" />
    </div>
    <van-cell center clickable title="点击显示更多内容" @click="toShow">
    </van-cell>
    <div v-show="needShow">
    <!-- 以下为隐藏选填内容 -->
    <!-- <van-collapse v-model="activeNames">
    <van-collapse-item title="点击显示更多内容" name="1"> -->
      <!-- 组修 -->
    <van-field readonly clickable placeholder="组修出席了吗？" label="组修" colon :value="zuxiu" @click="zuBoolean = true" />
    <van-action-sheet v-model="zuBoolean" :actions="zuActions" @select="zuOnSelect" />
    <!-- 班修 -->
    <van-field readonly clickable placeholder="班修出席了吗？" label="班修" colon :value="banxiu" @click="banBoolean = true" />
    <van-action-sheet v-model="banBoolean" :actions="banActions" @select="banOnSelect" />
      <!-- 慈经 -->
    <van-field readonly clickable :value="cijing" label="慈经" colon placeholder="请选择慈经遍数" @click="($event) => {fieldClick($event, 'showCijing')}" />
    <van-popup v-model="showCijing" round position="bottom" @click="($event) => {getMyValue($event,'showCijing')}">
      <van-picker visible-item-count="7" :default-index="defaultIndex" title="慈经遍数" :columns="cijingColumns"  
       @change="valueChange" ref ="cijingPicker"/>
    </van-popup>
      <!-- 自修遍数 -->
    <van-field readonly clickable :value="zixiu" label="自修遍数" colon placeholder="请选择自修遍数" @click="($event) => {fieldClick($event, 'showZixiu')}" />
    <van-popup v-model="showZixiu" round position="bottom" @click="($event) => {getMyValue($event,'showZixiu')}">
      <van-picker visible-item-count="7" :default-index="defaultIndex" title="自修遍数" :columns="zixiuColumns" 
       @change="valueChange" ref ="zixiuPicker"/>
      </van-popup>
    <!-- 服务大众 -->
     <!-- <van-field v-model="fuwu" label="服务大众" colon placeholder="请输入服务大众时长" type="digit"/> -->
    <van-field readonly clickable :value="fuwu" label="服务时长" colon placeholder="请选择服务大众时长" @click="($event) => {fieldClick($event, 'showFuwu')}" />
    <van-popup v-model="showFuwu" round position="bottom" @click="($event) => {getMyValue($event,'showFuwu')}">
      <van-picker visible-item-count="10" :default-index="defaultIndex" title="服务时长" :columns="fuwuColumns" 
       @change="valueChange" ref ="fuwuPicker"/>
      </van-popup>

         <!-- 服务项目  无需确定版-->
    <van-field readonly clickable :value="cishan" label="服务项目" colon placeholder="请选择服务大众项目" @click="($event) => {fieldClick($event, 'showCishan')}" right-icon="question-o" @click-right-icon.stop="showAnswer"/>
    <van-popup v-model="showCishan" round position="bottom" @click="($event) => {getMyValue($event,'showCishan')}">
      <van-picker title="服务项目" :columns="cishanColumns"  
      @change="valueChange" ref ="cishanPicker"/>
    </van-popup>
     <!-- 服务项目 点击确定版-->
    <!-- <van-field readonly :value="cishan" label="服务项目" colon placeholder="请选择服务大众项目" @click="showCishan = true" right-icon="question-o" @click-right-icon.stop="showAnswer"/> 
    <van-popup v-model="showCishan" round position="bottom" >
      <van-picker show-toolbar title="服务项目" :columns="cishanColumns"  
      @confirm="fuwuClick" ref ="cishanPicker" @cancel="($event) => {isCancel($event, 'showCishan')}"/>
    </van-popup> -->
    
     <!-- 引导吃素 -->
    <!-- <van-field v-model="yindao" label="引导吃素" colon placeholder="请输入引导吃素次数" type="digit"/> -->
    <van-field readonly clickable :value="yindao" label="引导吃素" colon placeholder="请选择引导吃素次数" @click="($event) => {fieldClick($event, 'showYindao')}"/>
    <van-popup v-model="showYindao" round position="bottom" @click="($event) => {getMyValue($event,'showYindao')}">
      <van-picker visible-item-count="7" :default-index="defaultIndex" title="引导次数" :columns="yindaoColumns"  
      @change="valueChange" ref ="yindaoPicker"/>
    </van-popup>

     <!-- 传灯邀请 -->
    <!-- <van-field v-model="chuandeng" label="传灯邀请" colon placeholder="请输入传灯邀请次数" type="digit"/> -->
    <van-field readonly clickable :value="chuandeng" label="传灯邀请" colon placeholder="请选择传灯邀请次数" @click="($event) => {fieldClick($event, 'showChuandeng')}"/>
    <van-popup v-model="showChuandeng" round position="bottom" @click="($event) => {getMyValue($event,'showChuandeng')}">
      <van-picker visible-item-count="10" :default-index="defaultIndex" title="传灯邀请次数" :columns="chuandengColumns"  
      @change="valueChange" ref ="chuandengPicker"/>
    </van-popup>
    
    <!-- 本周列提纲 -->
    <van-field readonly clickable placeholder="本周列提纲了吗？" label="列提纲" colon :value="tigang" @click="tigangBoolean = true" />
    <van-action-sheet v-model="tigangBoolean" :actions="tigangActions" @select="tigangOnSelect" />
    <!-- 举办读书会 -->
    <!-- <van-field v-model="dushu" label="举办读书会" colon placeholder="请输入举办读书会次数" type="digit"/> -->
    <van-field readonly clickable :value="dushu" label="举办读书会" colon placeholder="请选择举办读书会次数" @click="($event) => {fieldClick($event, 'showDushu')}"/>
    <van-popup v-model="showDushu" round position="bottom" @click="($event) => {getMyValue($event,'showDushu')}">
      <van-picker visible-item-count="7" :default-index="defaultIndex" title="读书会次数" :columns="dushuColumns"  
      @change="valueChange" ref ="dushuPicker"/>
    </van-popup>

    <van-field readonly clickable :value="tougao" label="网站投稿" colon placeholder="请选择网站投稿次数" @click="($event) => {fieldClick($event, 'showTougao')}"/>
    <van-popup v-model="showTougao" round position="bottom" @click="($event) => {getMyValue($event,'showTougao')}">
      <van-picker visible-item-count="7" :default-index="defaultIndex" title="投稿次数" :columns="tougaoColumns"  
      @change="valueChange"  ref ="tougaoPicker"/>
    </van-popup>  
    <!-- </van-collapse-item>
    </van-collapse> -->
    </div>
  <div style="margin: 16px;">
    <van-button round block type="info" native-type="submit">提交</van-button>
  </div>
  </van-form>
  <!-- 提示内容展示 -->
    <van-popup v-model="showSm" @click="showSm = false" :style="{ width: '90%' }">
      <div class="wrapper">
      <van-cell-group inset>
        <span v-for="item in cishanColumns.slice(0,-1)" :key="item.text">
          <h1>{{item.text}}</h1>
          <van-cell v-for="t in item.children.slice(1)" :key="t.text" :title="t.text" :label="t.value"/>
        </span>
      </van-cell-group>
    </div>
    </van-popup>
  <van-dialog v-model="showDailog" title ="    
      "  @confirm="() => {chargeBtn(mykey)}" >
      <van-field v-model="myValue" rows="1" autosize label="请输入" colon :placeholder="tishi" :type="myType"/>
    </van-dialog>
  <van-dialog v-model="showWeekData" title="本周累计数据" confirm-button-text="复制" :message="warnMsg" @confirm="copyData" />
  </div>
</template>

<script>
export default {
  name: 'MyVantForm',
  data () {
    return {
      userInfo: '',
      classValue:'',
      showClass:false,
      classColumns: ['请选择'],
      activeNames: [],
      show:false,
      date:'',
      minDate: this.getDate(-7),
      maxDate: this.getDate(0),
      defaultIndex:2,
      // 姓名
      name:'',
      showName:false,
      nameColumns:['请选择'],
      // 定课
      dingke:'',
      showDingke:false,
      dingkeColumns:['请选择',"1","2","3","4","5","6","7","8","9","10"],
      // 闻思
      wensi:'',
      showWensi:false,
      wensiColumns:['请选择','10','20','30','40','50','60','70','80','90','100','120','140','180','200','其他'],
      // 慈经遍数
      cijing:'',
      showCijing:false,
      cijingColumns:['请选择','1','2','3','4','5',],

      // 原文朗诵
      langsong:'',
      showLangsong:false,
      langsongColumns:['请选择','1','2','3','4','5'],

      // 菩提导航打卡遍数
      daka:'',
      showDaka:false,
      dakaColumns:['请选择','1','2','3','4','5','6','7','8','9','10'],

      needShow:false,
      mycount: '',

      // 一日一转 是否
      showBoolean:false,
      actions: [{ name: '是' }, { name: '否' }],
      yiri:'否',

      zixiu:'',
      showZixiu:false,
      zixiuColumns:['请选择','1','2','3','4','5'],
      // 引导吃素
      yindao:'',
      showYindao:false,
      yindaoColumns:['请选择','1','2','3','4','5'],

      // 网站投稿次数
      // tougaoBoolean:false,
      // tougaoActions: [{ name: '是' }, { name: '否' }],
      tougao:'',
      showTougao:false,
      tougaoColumns:['请选择','1','2','3','4','5'],

      // 服务时长
      fuwu:'',
      showFuwu:false,
      fuwuColumns:['请选择','1','2','3','4','5','6','7','8','9','10','其他'],

      // fuwuneirong:'',
      // 读书会次数
      dushu:'',
      showDushu:false,
      dushuColumns:['请选择','1','2','3','4','5'],

      // 服务项目
      cishan:'',
      showCishan:false,
      // cishanColumns:['请选择','护持读书会','临终关怀','临终助念','疾病关怀','修学关怀','健康养生','班级庆生','班级慈善活动(非庆生)','数据义工','其他'],
      cishanColumns:[
        {
          'text':'辅导',
          'children':[{'text':'请选择','value':''},{'text':'选拔','value':''},{'text':'辅导员成长','value':'辅导员跟班定课、辅导员学习、路径宣导、带班备课、辅导员八三养成营'}]
        },
        {
          'text':'传灯',
          'children':[{'text':'请选择','value':''},{'text':'读书会','value':'护持、主持读书会、书友回访、传灯例会'},{'text':'文宣','value':''},
          {'text':'拓展','value':''},{'text':'开班','value':''},{'text':'传灯例会','value':''}]
        },
        {
          'text':'学员服务',
          'children':[{'text':'请选择','value':''},{'text':'修学过程服务','value':'数据义工、app开发、修学关怀'},
          {'text':'生命关怀','value':'疾病关怀、临终关怀、助念'},
          {'text':'班级慈善','value':'班级庆生、班级慈善'},{'text':'健康养生','value':''}]
        },
        {
          'text':'知察',
          'children':[{'text':'请选择','value':''},{'text':'安全知察','value':''}]
        },
        {
          'text':'经营',
          'children':[{'text':'请选择','value':''},{'text':'人才成长','value':''},{'text':'团队建设','value':'班长例会、班委会'},
          {'text':'孵化','value':''},{'text':'人文空间运营','value':''}]
        },
        {
          'text':'其他',
          'children':[{'text':'','value':''}]
        },
      ],
      // 传灯邀请次数
      chuandeng:'',
      showChuandeng:false,
      chuandengColumns:['请选择','1','2','3','4','5','6','7','8','9','10','其他'],

      banBoolean:false,
      banActions: [{ name: '是' }, { name: '否' }],
      banxiu:'否',
      zuBoolean:false,
      zuActions: [{ name: '是' }, { name: '否' }],
      zuxiu:'否',
      tigangBoolean:false,
      tigangActions: [{ name: '是' }, { name: '否' }],
      tigang:'否',

      // onchange变化值
      myChange:'',
      // 输入其他的自定义值
      showDailog:false,
      myValue:'',
      mykey:'',
      tishi:'请输入值',
      myType:'number',

      // 本周累计数据
      showWeekData:false,
      weekData:'',
      msg:'',
      // 班级启动时间
      runDate:'',
      warnMsg:'',
      // 服务项目提示
      showSm:false,
      xm1:"泉州是闻名海内外的国际花园城市，中国三大金融综合改革试验区之一，海峡西岸经济区五大中心城市之一，经济总量曾连续22年居福建省首位。",
      xm2:[''],
      // 附带数据
      myIp:returnCitySN['cip'],
      begin:'',
      end:'',
      formTime: 0,
      myPhone:this.getMyPhone()
    }
  },
  created(){
    this.mycount = 0
    this.begin = Date.parse( new Date());
    var user = localStorage.getItem('user');
    console.log("首次登录获取缓存用户名：",user)
    var clsName = localStorage.getItem('classValue')
      console.log('本地缓存班级：',clsName)
      if (clsName != null){
        if (clsName.search("HJ_") != -1){
          this.classValue = "濠江班小组" + clsName.split('_')[1]
          localStorage.setItem('classValue', this.classValue)
        }else{
          this.classValue = clsName
        }
      }
    if(user != null){
      this.name = user
    }
    this.$axios.get('/api/get_class').then((res)=>{
      var mydata = res.data;  
      this.userInfo = eval('(' + mydata + ')');
      console.log('获取班级数据:',this.userInfo)
      for(var cls in this.userInfo) {
        this.classColumns.push(cls)
      }
      if(this.classValue.length>0){
        for (var i in this.userInfo[this.classValue]){
          if (typeof this.userInfo[this.classValue][i]  == 'string') {
             this.nameColumns.push(this.userInfo[this.classValue][i])
          }
         
        }
        
      }
    })
    
  },
  methods:{
        // 需要做跨域处理
    getMyPhone(){
      Array.prototype.contains = function(needle) {
        for (i in this) {
          if (this[i].indexOf(needle) > 0)
            return i;
        }
        return -1;
      }

      var device_type = navigator.userAgent; //获取userAgent信息
      // document.write(device_type); //打印到页面
      var md = new MobileDetect(device_type); //初始化mobile-detect
      var os = md.os(); //获取系统
      var sys_name = os
      var model = "";
      if (os == "iOS") { //ios系统的处理
        os = +md.version("iPhone");
        console.log('系统名：',os)
        model = md.mobile() + ' '+ sys_name;
      } else if (os == "AndroidOS") { //Android系统的处理
        os = md.os() + md.version("Android");
        var sss = device_type.split(";");
        var i = sss.contains("Build/");
        if (i > -1) {
          model = sss[i].substring(0, sss[i].indexOf("Build/"));
        }
      }
      // alert(os + "---" + model);//打印系统版本和手机型号
      // model + ' ' + sys_name + ''+ os  
      console.log(model + ' ' + os, '打印系统版本和手机型号')
      return model + ' ' + os
      
    },
    toShow(){
      let num = this.mycount;
      // console.log(num)
      num += 1
      this.mycount = num
      // console.log(this.mycount)
      // this.clickNum = Number(num)
      if (this.mycount % 2 == 0){
        this.needShow = false
      }else{
        this.needShow = true
      }
      // console.log('是否显示:',this.needShow)

    },
    showAnswer(){
      this.showSm = true
      this.getMyPhone()
      console.log("this is my answer !",this.myPhone)
    },
    isDate(){
      if (this.name == ''){
        this.$toast('请先选择班级和法名');
        this.show = false
      }
      this.show = true
      
    },
    onOpen(){
      this.$nextTick(() => {
        if (document.getElementsByClassName('van-calendar__body')[0]) {
            const back = document.getElementsByClassName('van-calendar__body')[0].scrollTop;
            document.getElementsByClassName('van-calendar__body')[0].scrollTop = back - 10;
            setTimeout(() => {
                document.getElementsByClassName('van-calendar__body')[0].scrollTop = back;
            }, 10);
      }
 });
    },
    isCancel($event,showType){
      var myIndex = {'classValue':'showClass','name':'showName', 'dingke':'showDingke', 'wensi':'showWensi','cijing':'showCijing', 'langsong':'showLangsong', 
      'daka':'showDaka', 'yindao':'showYindao', 'tougao':'showTougao', 'fuwu':'showFuwu', 'dushu':'showDushu', 
      'cishan':'showCishan',  'chuandeng':'showChuandeng','zixiu':'showZixiu'}
      for(var key in myIndex){
        if(showType == myIndex[key]){
          this[key] = "";
          this[showType] = false
        }
      }
    },
    // 服务项目 点击确认版本
    fuwuClick(value){
      this.showCishan = false
      this.tishi = "其他服务项目"
      console.log('value',value)
      if(value[0] == '其他'){
        this.myType = 'text'
        this.myValue = ''
        // 如果值为其他，那么弹出对话框，并设置值为对话框输入值
        this.mykey = 'cishan'
        this.showDailog = true
        this.cishan = this.myValue
      }
      if(value[1] == '请选择'){
        this.cishan = value[0]
      }else{
        this.cishan = value[1]
      }
    },
    fieldClick($event,myshow){
      console.log('当前触发field:', myshow)
      this[myshow] = true
      var refsName = myshow.toLowerCase().slice(4) + 'Picker'
      var myColumns = myshow.toLowerCase().slice(4) + 'Columns'
      console.log("字符串拼接",this.$refs[refsName])
      if (myshow == 'showClass'){
          this.name = ''
          this.nameColumns = ['请选择']
        }
      if (myshow == 'showName'){
          if (this.classValue == ''){
            this.$toast('请先选择班级');
            this.showName = false
          }
      }
      if (this.$refs[refsName]){
        if(myshow == 'showCishan'){
          if (this.$refs[refsName].getValues()[0].text == '其他'){
            this.myChange = ['其他','']
          }else{
            this.myChange = [this.$refs[refsName].getValues()[0].text,this.cishan]
          }
        }else{
          this.myChange = this.$refs[refsName].getValues()[0]

        }
        console.log('再次触发时的值',this.myChange)
      }else{
        this.myChange=this[myColumns][this.defaultIndex]
        if (myshow == 'showCishan'){
          // 第一次
          this.myChange = [this[myColumns][0].text,this[myColumns][0].children[0].text]
        }
        console.log('首次触发时的值：', this.myChange)
      }
    },
    // 传入值与节点，根据节点进行赋值，定义节点键值对
    // 触发值改变，调用弹出层点击事件，将改变的值进行赋值，并关闭picker
    // 需要将值传入click事件中
    valueChange(picker,value){
      // this.myChange = ''
      var myIndex = {'班级':'classValue','法名':'name','定课遍数':'dingke','闻思时间':'wensi','诵读遍数':'langsong','打卡遍数':'daka',
      '慈经遍数':'cijing','自修遍数':'zixiu','服务时长':'fuwu','服务项目':'cishan','引导次数':'yindao','传灯邀请次数':'chuandeng',
      '读书会次数':'dushu','投稿次数':'tougao'}
      // console.log('获取到的值')
    
        if (value == '请选择'){
          this.myChange = ''
        }else{
          this.myChange = value
        }

      console.log("aaaaa:", value)
      // console.log(this.$refs.showwensi)
      // for (var key in myIndex){
      //   if (key == picker.title){
      //     this[myIndex[key]] = value
      //     console.log('赋值：',myIndex[key], this[myIndex[key]])
      //   }
      // }
    },
    // 触发click 后确认值, mychange 已经确认
    getMyValue($event,myshow){

      var myIndex = { 'dingke':'showDingke', 'wensi':'showWensi','cijing':'showCijing', 'langsong':'showLangsong', 
      'daka':'showDaka', 'yindao':'showYindao', 'tougao':'showTougao', 'fuwu':'showFuwu', 'dushu':'showDushu', 
      'cishan':'showCishan',  'chuandeng':'showChuandeng','zixiu':'showZixiu','classValue':'showClass','name':'showName'}
      var tishiDict = {
        'showCishan':'其他服务项目','showWensi':'闻思时长（分钟）','showFuwu':'服务时长（小时）','showChuandeng':'传灯邀请次数'
      }
      // 其他选项是弹出自定义框,定义提示语
      for (var k in tishiDict){
        if (myshow == k){
          this.tishi = tishiDict[k]
        }
      }
      for (var key in myIndex){
        if (myshow == myIndex[key]){
            if (key == 'cishan'){
              if(this.myChange[1] == '请选择' || this.myChange[1] == ''){
                this[key] = this.myChange[0]
              }else{
                this[key] = this.myChange[1]
              }
            }else{
              this[key] = this.myChange
            }
            this[myshow] = false
            console.log('我的项目为：',this[key])
            if(key == 'name'){
              localStorage.setItem('user',this[key])
              localStorage.setItem('classValue',this.classValue)
              if (this.date != ''){
                this.check_today()
              }
            }
            if (key == 'classValue'){
              for (var i in this.userInfo[this.classValue]){
                if (typeof this.userInfo[this.classValue][i]  == 'string') {
                  this.nameColumns.push(this.userInfo[this.classValue][i])
                }
                // this.nameColumns.push(this.userInfo[this.classValue][i])
              }
            }
            if (this[key] == '其他'){
              if(myshow == 'showCishan'){
                this.myType = 'text'
              }else{
                this.myType = 'number'
              }
              this.myValue = ''
              // 如果值为其他，那么弹出对话框，并设置值为对话框输入值
              this.mykey = key
              this.showDailog = true
              this[key] = this.myValue
            }
            // else{
            //   this.myChange = ''
            // }
            
          }
      }
    },

    chargeBtn(mykey) {
      this.showDailog = false;
      if (this.myValue == ''){
        if(mykey == 'cishan'){
          this.tishi = "其他服务项目"
          this[mykey] = this.tishi
        }
        this.myChange = '其他'
      }else{
        this.myChange = ''
        this[mykey] = this.myValue
      }
    },
    check_today(){
      var dd = {"name":this.name, "mydate":this.date,"myclass":this.classValue}
      this.$axios({
        method:'post',
        url:'/api/check_today',
        data:dd
      }).then(res => {
        var myResult = res.data.result.data
        this.runDate = res.data.result.run_date
        console.log("this.runDate",this.runDate)
        if (myResult !== true){
          for(var key in myResult){
            if (myResult[key] === true){
              this[key] = '是'
            }else if (myResult[key] === false){
              this[key] = '否'
            }else{
              this[key] = myResult[key]
            }
          }
          this.$toast.fail('所选日期已打卡。如需更新，请在此基础上修改！');
        }else{
          this.initValue()
        }
      })
    },
    initValue(){
      this.dingke = ''
      this.wensi = ''
      this.cijing = ''
      this.langsong = ''
      this.daka = ''
      this.yiri = '否'
      this.zixiu = ''
      this.yindao = ''
      this.tougao = ''
      this.fuwu = ''
      this.dushu = ''
      this.cishan = ''
      this.chuandeng = ''
      this.banxiu = '否'
      this.zuxiu = '否'
      this.tigang = '否'
    },
    onName(value) {
      this.name = value;
      this.showName = false;
      localStorage.setItem('user',this.name)

    },
    formatDate(date) {
      return `${date.getFullYear()+'-'+(date.getMonth()+1)+'-'+ date.getDate()}`;
    },
    setMyDate(date){
      // 将date 与今天做一个比较

      var d = new Date() - date;
      this.date = this.formatDate(date);
      if (d > 172800000){
        this.$toast.fail('所选日期偏离较远，请留意是否有误。')
        this.show = false;
      }
      this.show = false;
      this.check_today()
    },
    compartDate(){
      // 将2022-05-11格式字符串转成时间
      var run_date = new Date(Date.parse(this.runDate.replace(/-/g,"/")));
      console.log('时间相减：',new Date() > run_date)
      return new Date() > run_date ? true : false;
    },

    onSelect(item) {
      this.showBoolean = false;
      this.yiri = item.name
    },
    banOnSelect(item) {
      this.banBoolean = false;
      this.banxiu = item.name
    },
    zuOnSelect(item) {
      this.zuBoolean = false;
      this.zuxiu = item.name
    },
    tigangOnSelect(item) {
      this.tigangBoolean = false;
      this.tigang = item.name
    },
    writeTime(){
      this.end = Date.parse( new Date());
      var write_time = (this.end - this.begin)/1000
      console.log('开始时间：', this.begin,'; 结束时间：',this.end, ';相差时间:',write_time)
      return write_time
    },
    // 表单提交
    onSubmit(){
      var axios = require('axios');
      this.formTime = this.writeTime()
      var data = {'mydata':
        {"name":this.name,'my_class':this.classValue, "dingke": this.dingke, "date":this.date,"wensi":this.wensi,"cijing":this.cijing,"langsong":this.langsong,
        "daka":this.daka,"yiri":this.yiri,"zixiu":this.zixiu, "yindao":this.yindao,"tougao":this.tougao,"fuwu":this.fuwu,"dushu":this.dushu,
        "cishan":this.cishan,"chuandeng":this.chuandeng,"banxiu":this.banxiu,"zuxiu":this.zuxiu,"tigang":this.tigang,
        "write_ip":this.myIp,"write_time":this.formTime,"write_device":this.myPhone
      }};
      var config = {
        method: 'post',
        url: '/api/submit_myform',
        data: data
      };
      if (this.name == '' || this.date == '' || this.classValue == ''){
        this.$toast('请选择班级、法名和考核日期');
      }
      else {
        axios(config).then(res => {
          // 提交返回值。根据返回值提醒用户。
          var reData = res.data.result
          console.log(reData)
          this.$toast.loading("提交中")
          clearTimeout(this.timer);  //清除延迟执行 
          this.timer = setTimeout(()=>{   //设置延迟执行
              this.$toast.clear();
              this.weekData = reData.msg
              console.log(this.weekData)
              this.warnMsg = this.compartDate() ? this.weekData : `${this.weekData} \n———————\n本班打卡正式启动日期为${this.runDate}，在这之前的数据属于测试数据，过后会删除，请知悉！` ;
              
              this.showWeekData = true
              // this.$router.push({name:'PuTiForm', params:{msg:reData.msg}})
          },1000);   
        })
      }
    },

    getDate(index){
    var date = new Date(); 
    var newDate = new Date();
    newDate.setDate(date.getDate() + index);
    var timeList = [newDate.getFullYear(),(newDate.getMonth()),newDate.getDate()];
    return new Date(timeList[0],timeList[1],timeList[2]);
    },
    copyData(){
      try{
        this.$copyText(this.weekData).then(res =>{
        this.$toast.success("周数据复制成功");
      })
      }catch(e){
        console.log("error:",e)
        this.$toast.fail("当前浏览器不支持复制")
      }      
      this.showWeekData = false
    }
  },
}
</script>
<style>
.formDiv {
  margin-left: 2%;
  margin-right: 2%;
  border: none;
}
.van-calendar__popup.van-popup--bottom, .van-calendar__popup.van-popup--top{
    height: 90% !important;
}
.van-cell__label{
  color: red !important;
}
.wrapper {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    background-color: #fff;
  }
</style>
