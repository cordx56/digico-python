<template lang="pug">
  .digico
    b-card.mb-3(header="実行結果", header-text-variant="white", header-bg-variant="primary", align="center", v-if="answer", :title="answer[0]['a']")
      b-table-simple(striped)
        b-tbody(v-for="(ans, index) in answer")
          b-tr
            b-th(rowspan="2") {{ index + 1 }}
            b-td(colspan="2") {{ ans['a'] }}
          b-tr
            b-td(style="position: relative;")
              .bgCosBar(:style="'width: ' + (ans['cos'] * 100) + '%;'")
              .cosText(style="position: relative;") {{ ans['cos'] }}
            b-td {{ ans['q'] }}
    b-form(@submit.prevent="getAnswer")
      b-form-group(label="Question: ")
        b-form-input(v-model="form.qtext", type="text", required)
      b-form-group
        b-button(type="submit", variant="primary", :disabled="voiceRecog.running") 質問送信
    b-card(header="音声認識", header-text-variant="white", header-bg-variant="info", align="center")
      span(v-if="voiceRecog.obj")
        b-button.mr-4(@click="runVoiceIdle", variant="success") 認識待機
        b-button(@click="runVoiceQuestion", variant="warning") 強制実行
      span(v-else)
        | 非対応ブラウザです
</template>

<script>

export default {
  name: 'digicoForm',
  data() {
    return {
      answer: null,
      form: {
        qtext: ''
      },
      voiceRecog: {
        cls: window.SpeechRecognition || window.webkitSpeechRecognition,
        obj: null,
        running: false,
        idling: false,
        question: false
      }
    }
  },
  methods: {
    runVoiceIdle() {
      try {
        this.voiceRecog.obj.stop()
      } catch (e) {
        console.log(String(e))
      }
      this.voiceRecog.obj.continuous = true
      this.voiceRecog.obj.onresult = (event) => {
        var res = event.results[event.results.length - 1][0].transcript
        this.form.qtext = res
        if ((res.indexOf('ねえ') > -1 || res.indexOf('ねぇ') > -1) && (res.indexOf('でじこ') > -1 || res.indexOf('デジコ') > -1)) {
          this.runVoiceQuestion()
        }
      }
      this.idling = true
      try {
        this.voiceRecog.obj.start()
      } catch (e) {
        console.log(String(e))
      }
    },
    runVoiceQuestion() {
      try {
        this.voiceRecog.obj.stop()
      } catch (e) {
        console.log(String(e))
      }
      this.voiceRecog.obj.continuous = false
      this.voiceRecog.obj.onresult = (event) => {
        var res = event.results[event.results.length - 1]
        this.form.qtext = res[0].transcript
        if (res.isFinal) {
          this.getAnswer()
          if (this.idling) this.runVoiceIdle()
        }
      }
      try {
        this.voiceRecog.obj.start()
      } catch (e) {
        console.log(String(e))
      }
    },
    getAnswer() {
      this.$axios.get('/api/v1/answer', {
        params: {
          q: this.form.qtext
        }
      }).then((response) => {
        if (response.data.status) {
          this.answer = response.data.answer.slice(0, 5)
          var ae = new Audio();
          ae.src = "/voice?text=" + encodeURI(this.answer[0]['a'])
          ae.play()
        } else {
          window.alert(response.data.message)
        }
      }).catch((error) => {
        window.alert(String(error))
      })
    },
    stopVoiceRecog() {
      try {
        this.voiceRecog.obj.stop()
      } catch (e) {
        console.log(String(e))
      }
    }
  },
  mounted() {
    this.voiceRecog.obj = new this.voiceRecog.cls()
    this.voiceRecog.obj.interimResults = true
    this.voiceRecog.obj.lang = 'ja-JP'
  }
}
</script>

<style lang="scss" scoped>
.bgCosBar {
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  background-color: #9cf;
}
</style>
