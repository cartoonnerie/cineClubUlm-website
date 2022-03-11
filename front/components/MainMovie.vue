<template>
  <div class="main-movie rounded border bg-white overflow-hidden shadow">
    <img
      class="main-movie__poster"
      src="https://m.media-amazon.com/images/I/71bmNSxkw-L._AC_SY550_.jpg"
    />
    <div
      class="main-movie__description flex flex-col justify-between p-8 space-y-5"
    >
      <div class="text-4xl">{{ title }}</div>
      <div>
        Durée :125 minutes<br />
        Noir et blanc<br />
        Pays :USA<br />
        35mm . VOSTFR<br />
        Année :1960<br />
        Avec :Jack Lemmon, Shirley MacLaine, Fred MacMurray, Ray Walston<br />
      </div>
      <div class="text-3xl">
        {{ formattedDate }}
      </div>
    </div>
    <MovieDetailsModal />
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: "Harry Potter à l'école des sorciers",
      date: new Date(2021, 7, 26, 20, 30),
    }
  },
  computed: {
    formattedDate() {
      const date = this.date.toLocaleDateString("fr-FR", {
        weekday: "long",
        year: "numeric",
        month: "long",
        day: "numeric",
      })
      const hour = this.date
        .getHours()
        .toLocaleString("fr-FR", { minimumIntegerDigits: 2 })
      const minute = this.date
        .getMinutes()
        .toLocaleString("fr-FR", { minimumIntegerDigits: 2 })
      const time = `${hour}h${minute}`

      return `${date} à ${time}`
    },
  },
}
</script>

<style>
.main-movie {
  @apply flex justify-between;
}

.main-movie__poster {
  @apply w-72;
}
</style>
