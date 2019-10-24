<template lang="pug">
  #app
    b-navbar(toggleable="md", type="dark", variant="dark")
      b-container
        b-navbar-brand(href="https://digico.cordx.net/") digiCo
        b-navbar-toggle(target="nav-collapse")
        b-collapse#nav-collapse(is-nav)
          b-navbar-nav.ml-auto
            b-nav-item(to="/about") About
            b-nav-item(href="https://github.com/cordx56/digico-python", target="_blank")
              | Repository
    router-view.mt-4
</template>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

</style>
