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
    <template v-if="failed">
      <div class="q-mt-lg" style="color: red">
        Sorry, e-mail or password is wrong.
      </div>
    </template>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import {
  signInWithEmailAndPassword,
  browserLocalPersistence,
} from 'firebase/auth';
import { auth } from 'boot/firebase';

const router = useRouter();

const email = ref('dakken205de@gmail.com');
const password = ref('depptxmaker241212432');
const failed = ref(false);

const login = () => {
  failed.value = false;
  auth.setPersistence(browserLocalPersistence).then(() => {
    return signInWithEmailAndPassword(auth, email.value, password.value)
      .then(() => {
        router.push('/');
      })
      .catch(() => {
        failed.value = true;
        password.value = '';
      });
  });
};
</script>
