<template lang="pug">
  b-container.text-center
    b-row.mb-4
      b-col.mb-3(cols="12", lg="4")
        img(:src="mainImageSrc")
      b-col(cols="12", lg="8")
        DigicoForm.mb-4(@updateImage="updateMainImage")
        DocumentsLink
        AboutInfo
</template>

<script>
import DigicoForm from '@/components/DigicoForm.vue'
import DocumentsLink from '@/components/DocumentsLink.vue'
import AboutInfo from '@/components/AboutInfo.vue'

export default {
  name: 'home',
  components: {
    DigicoForm,
    DocumentsLink,
    AboutInfo
  },
  data() {
    return {
      mainImageSrc: require('@/assets/img/SAKURAdigico-sleep.png')
    }
  },
  methods: {
    updateMainImage(src) {
      this.mainImageSrc = require('@/assets/img/' + src)
    }
  }
}
</script>

<style lnag="scss" scoped>
img {
  max-width: 100%;
}
</style>
