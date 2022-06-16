<template>
 <div>
  <van-empty
  class="custom-image"
  :image="require('../assets/success.png')"
  description="提交成功，感谢您的打卡记录~"
/>
  <van-button round  type="primary" @click="showData">查看周数据</van-button>
   <van-dialog v-model="showWeekData" title="本周累计数据" confirm-button-text="复制" :message="weekData" @confirm="copyData" />
 </div>
</template>

<script>
export default {
  name: 'PuTiForm',
  data () {
    return {
      showWeekData:false,
      weekData:''
    }  
  },
  methods: {
    showData(){
      this.weekData = this.$route.params.msg
      console.log('周数据',this.weekData)
      this.showWeekData = true
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
  }
}
</script>
<style>
  .custom-image .van-empty__image {
    /* width: 160px;
    height: 160px; */
    max-width: 100%;
  }
</style>

