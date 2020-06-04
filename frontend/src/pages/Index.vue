<template>
  <div>
    <mavon-editor v-model="value" @save="save"/>
    <p>====</p>
    <vue-markdown>{{value}}</vue-markdown>
  </div>

</template>

<script>
import VueMarkdown from 'vue-markdown'

export default {
  name: 'Index',
  data: function () {
    return { value: '# 你好\n' + '- 泡泡\n' + '- 看看^上角标^\n' + '## 二级标题' }
  },
  methods: {
    // 尝试save事件
    save (md, html) {
      console.log(this.value)
      // console.log(this.title)
    }
  },
  components: {
    VueMarkdown
  }
}

</script>
