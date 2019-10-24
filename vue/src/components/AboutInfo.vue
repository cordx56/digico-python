<template lang="pug">
  .aboutInfo
    h3 About
    p 
      | Repository: 
      a(href="https://github.com/cordx56/digico-python", target="_blank") cordx56/digico-python
    h3 Software
    b-table(:items="depend")
</template>

<script>
export default {
  data() {
    return {
      depend: [
        {
          name: 'Open JTalk'
        }
      ]
    }
  }
}
</script>
