<template lang="pug">
  .aboutInfo
    h1 About
    p Author: cordx56
    p 
      | Repository: 
      a(href="https://github.com/cordx56/digico-python") cordx56/digico-python
    h1 Software
    b-table(:items="depend")
</template>

<script>
export default {
  data() {
    return {
      depend: [
        {
          name: '<a href="http://open-jtalk.sp.nitech.ac.jp/">Open JTalk</a>'
        }
      ]
    }
  }
}
</script>
