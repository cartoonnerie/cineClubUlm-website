<template>
  <div class="header w-full h-48">
    <div class="overlay h-full from-gray-100 bg-gradient-to-t via-transparent">
      <div class="container mx-auto h-full flex flex-col justify-end p-5">
        <ul class="flex flex-row justify-between">
          <li v-for="(menuItem, index) of menuItems" :key="index">
            <nuxt-link :to="menuItem.link">
              {{ menuItem.label }}
            </nuxt-link>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      menuItems: [
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
      ],
    }
  },
}
</script>

<style scoped>
.header {
  background-image: url("/images/banner.jpg");

  @apply uppercase text-gray-600;
}
</style>
