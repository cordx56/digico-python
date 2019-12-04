<template lang="pug">
  section.docuemtsLink
    h3 Documents
    b-table-simple
      b-tbody
        b-tr
          b-th Name
          b-th Description
        b-tr(v-for="(v, k, i) in docslist", :key="i")
          b-td(v-if="v.link")
            a(:href="v.link", target="_blank") {{ v.name }}
          b-td(v-else) {{ v.name }}
          b-td {{ v.desc }}
</template>

<script>
export default {
  data() {
    return {
      docslist: [
        {
          name: 'tf-idfとWord2Vecの併用による文章間類似度判定の実装',
          link: 'https://speakerdeck.com/cordx56/tf-idftoword2vecfalsebing-yong-niyoruwen-zhang-jian-lei-si-du-pan-ding-falseshi-zhuang',
          desc: '発表資料 - April 22, 2019'
        }
      ]
    }
  }
}
</script>
