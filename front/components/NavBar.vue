<template>
  <nav class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <nuxt-link class="navbar-item" to="index">
        <img src="~/assets/img/logo.png" />
      </nuxt-link>
      <a
        role="button"
        class="navbar-burger"
        aria-label="menu"
        aria-expanded="false"
        @click="isBurgerOpen = !isBurgerOpen"
      >
        <!-- the next three lines are meant for the burger menu -->
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>

    <div class="navbar-menu" :class="{ 'is-active': isBurgerOpen }">
      <div class="navbar-start">
        <nuxt-link
          v-for="(menuItem, index) of menuItems"
          :key="index"
          class="navbar-item"
          :to="menuItem.link"
        >
          {{ menuItem.label }}
        </nuxt-link>
      </div>

      <div class="navbar-end">
        <div class="navbar-item">
          <a class="button is-light"> Log in </a>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
const menuItems = ref([
  {
    label: "Accueil",
    link: "/",
  },
  {
    label: "À venir",
    link: "/a-venir",
  },
  {
    label: "À props",
    link: "/a-propos",
  },
])

const isBurgerOpen = ref(false)
</script>

<style lang="sass" scoped>
@include desktop
  .navbar
    padding: 0 2rem

.navbar-item img
  object-fit: contain
  @include desktop
    max-height: 5rem
    padding: 0 // necessary ?
</style>
