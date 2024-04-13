<template>
  <div class="flex flex-center column window-height">
    <q-card class="q-pa-md q-pt-lg" style="width: 350px; height: 190px">
      <div class="column q-gutter-y-md">
        <div class="col row">
          <span class="col text-right q-pr-sm q-pt-sm">e-mail : </span
          ><q-input v-model="email" class="col-9" dense filled />
        </div>
        <div class="col row">
          <span class="col text-right q-pr-sm q-pt-sm">password : </span
          ><q-input v-model="password" class="col-9" dense filled />
        </div>
        <div class="col q-mt-xs">
          <q-btn
            @click="login"
            class="float-right"
            color="primary"
            style="width: 100px"
            >Login</q-btn
          >
        </div>
      </div>
    </q-card>
  </div>
</template>

<script setup lang="ts">
import { useQuasar } from 'quasar';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import {
  signInWithEmailAndPassword,
  browserLocalPersistence,
} from 'firebase/auth';
import { auth } from 'boot/firebase';

const $q = useQuasar();
const router = useRouter();

const email = ref('');
const password = ref('');

const login = () => {
  $q.loading.show({ message: 'ログイン中...' });
  auth.setPersistence(browserLocalPersistence).then(() => {
    return signInWithEmailAndPassword(auth, email.value, password.value)
      .then(() => {
        router.push('/');
        $q.notify({
          message: 'ログインしました',
          color: 'positive',
          position: 'top',
        });
      })
      .catch(() => {
        password.value = '';
        $q.notify({
          message: 'ユーザ名またはパスワードが違います',
          color: 'negative',
          position: 'top',
        });
      })
      .finally(() => {
        $q.loading.hide();
      });
  });
};
</script>
