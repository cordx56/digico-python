<template lang="pug">
  section.aboutInfo
    h3 About
    p 
      | Repository: 
      a(href="https://github.com/cordx56/digico-python", target="_blank") cordx56/digico-python
    p 
      | digiCo portal: 
      a(href="https://digico.digicre.net/", target="_blank") digiCo Project
    h3 Collaborator
    b-table-simple
      b-tbody
        b-tr
          b-th Name
          b-th Description
      b-tbody(v-for="con in collabo")
        b-tr
          b-td(v-if="con.link")
            a(:href="con.link", target="_blank") {{ con.name }}
          b-td(v-else) {{ con.name }}
          b-td {{ con.desc }}
    h3 Main dependencies
    b-table-simple
      b-tbody
        b-tr
          b-th Name
          b-th Description
      b-tbody(v-for="dep in deplist")
        b-tr
          b-td(v-if="dep.link")
            a(:href="dep.link", target="_blank") {{ dep.name }}
          b-td(v-else) {{ dep.name }}
          b-td {{ dep.desc }}
</template>

<script>
export default {
  data() {
    return {
      collabo: [
        {
          name: '雛美乃',
          link: 'https://hinamino.tumblr.com/',
          desc: 'Character design, main illustration'
        }
      ],
      deplist: [
        {
          name: 'MeCab',
          link: 'https://taku910.github.io/mecab/',
          desc: 'Japanese morphological analyzer, 日本語形態素解析器'
        },
        {
          name: 'CaboCha',
          link: 'https://taku910.github.io/cabocha/',
          desc: 'Japanese dependency structure analyzer, 日本語係り受け解析器'
        },
        {
          name: 'gensim',
          link: 'https://github.com/RaRe-Technologies/gensim',
          desc: 'Word2Vec library'
        },
        {
          name: 'Open JTalk',
          link: 'http://open-jtalk.sourceforge.net/',
          desc: 'Japanese text-to-speach system'
        },
        {
          name: 'MMDAgent',
          link: 'https://sourceforge.net/projects/mmdagent/',
          desc: 'Voice agent for Open JTalk'
        }
      ]
    }
  }
}
</script>
