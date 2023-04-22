<template>
  <router-view />
</template>

<script>
import { getAuth, signOut, setPersistence, browserLocalPersistence } from 'firebase/auth'
export default {
  async beforeCreate() {
    await setPersistence(getAuth(), browserLocalPersistence)
    const auth = getAuth()
    if (auth.currentUser == null) {
      signOut(auth).then(() => {
        this.$router.push('/login')
      }).catch((err) => {
        console.log(err)
      })
      this.$router.push('/login')
    }
  }
}
</script>

<style>
.border {
  border-bottom: solid 1px rgb(219, 219, 219);
}
</style>