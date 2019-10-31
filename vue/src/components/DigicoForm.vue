<template lang="pug">
  .digico
    b-card.mb-3(header="実行結果", header-text-variant="white", header-bg-variant="success", align="center", v-if="answer", :title="answer[0]['a']")
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
    b-card.mb-3(header="質問", header-text-variant="white", header-bg-variant="primary", align="center")
      b-form(@submit.prevent="getAnswer")
        b-form-group(label="計算手法")
          b-form-select(v-model="form.engineOpt.selected", :options="form.engineOpt.options", size="sm")
        b-form-group
          b-form-input(v-model="form.qtext", type="text", required, :disabled="this.voiceRecog.running")
        b-button(type="submit", :variant="form.submit.variant", :disabled="this.voiceRecog.running") {{ form.submit.text }}
    b-card(header="音声認識", header-text-variant="white", header-bg-variant="info", align="center")
      span(v-if="voiceRecog.obj")
        b-button.mr-4(@click="runVoiceIdle", variant="success") 認識待機
        b-button.mr-4(@click="runVoiceQuestion", variant="warning") 強制実行
        b-button(@click="stopVoiceRecog", variant="danger") 認識停止
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
        qtext: '',
        submit: {
          text: '質問送信',
          variant: 'primary'
        },
        engineOpt: {
          selected: 'trz',
          options: [
            { value: 'trz', text: 'Trazo (Default)' },
            { value: 'ibp', text: 'Ibpro' }
          ]
        }
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
      this.voiceRecog.obj.onend = () => {
        console.log('Restart voice recognition...')
        this.voiceRecog.obj.start()
      }
      this.voiceRecog.obj.onresult = (event) => {
        var res = event.results[event.results.length - 1][0].transcript
        this.form.qtext = res
        if ((res.indexOf('でじこ') > -1 || res.indexOf('デジコ') > -1)) {
          this.runVoiceQuestion()
        }
      }
      this.idling = true
      this.voiceRecog.running = true
      this.form.submit.text = '待機中'
      this.form.submit.variant = 'primary'
      try {
        this.voiceRecog.obj.start()
      } catch (e) {
        console.log(String(e))
      }
    },
    runVoiceQuestion() {
      this.voiceRecog.obj.abort()
      this.voiceRecog.obj.onresult = (event) => {
        var res = event.results[event.results.length - 1]
        this.form.qtext = res[0].transcript
        if (res.isFinal) {
          this.getAnswer()
          this.runVoiceIdle()
        }
      }
      this.voiceRecog.running = true
      this.form.submit.text = '認識中'
      this.form.submit.variant = 'danger'
      try {
        this.voiceRecog.obj.start()
      } catch (e) {
        console.log(String(e))
      }
    },
    stopVoiceRecog() {
      this.voiceRecog.obj.onend = null
      this.voiceRecog.running = false
      this.form.submit.text = '質問送信'
      this.form.submit.variant = 'primary'
      this.voiceRecog.obj.abort()
    },
    getAnswer() {
      this.$axios.get('/api/v1/answer', {
        params: {
          q: this.form.qtext,
          engine: this.form.engineOpt.selected
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
    }
  },
  mounted() {
    this.voiceRecog.obj = new this.voiceRecog.cls()
    this.voiceRecog.obj.interimResults = true
    this.voiceRecog.obj.continuous = true
    this.voiceRecog.obj.lang = 'ja-JP'
    //this.runVoiceIdle()
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
