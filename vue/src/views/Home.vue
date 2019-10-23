<template lang="pug">
  b-container
    b-row.mb-4
      b-col.mb-3(cols="12", lg="4")
        | image
      b-col(cols="12", lg="8")
        DigicoForm
    b-row
      b-col(cols="12")
        AboutInfo
</template>

<script>
import DigicoForm from '@/components/DigicoForm.vue'
import AboutInfo from '@/components/AboutInfo.vue'

export default {
  name: 'home',
  components: {
    DigicoForm,
    AboutInfo
  }
}
</script>
