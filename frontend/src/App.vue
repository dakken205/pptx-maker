<template>
  <router-view />
</template>

<script setup lang="ts">
import { useQuasar } from 'quasar';
import { useRouter } from 'vue-router';
import { auth } from 'boot/firebase';
import { browserLocalPersistence } from 'firebase/auth';

const $q = useQuasar();
const router = useRouter();

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some((record) => record.meta.requiresAuth);
  auth.setPersistence(browserLocalPersistence).then(() => {
    if (requiresAuth && !auth.currentUser) {
      $q.notify({
        color: 'negative',
        position: 'top',
        message: 'ログインが必要です',
      });
      next('/login');
    } else {
      next();
    }
  });
});
</script>
