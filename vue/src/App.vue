<template lang="pug">
  #app
    b-navbar(toggleable="md", type="dark", variant="dark", sticky)
      b-container
        b-navbar-brand(to="/") digiCo NLP
        b-navbar-toggle(target="nav-collapse")
        b-collapse#nav-collapse(is-nav)
          b-navbar-nav.ml-auto
            b-nav-item(to="/about") About
            b-nav-item(href="https://github.com/cordx56/digico-python", target="_blank")
              | Repository
    router-view.mt-4
</template>

<style lang="scss">
</style>
