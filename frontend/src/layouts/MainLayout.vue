<template>
  <q-layout view="hHh Lpr lff" container style="height: 100vh" class="">
    <q-header elevated :class="$q.dark.isActive ? 'bg-secondary' : 'bg-black'">
      <q-toolbar>
        <q-toolbar-title>DA研 定例会資料作成フォーム</q-toolbar-title>
        <q-btn flat @click="logout" round dense icon="logout" />
      </q-toolbar>
    </q-header>
    <q-page-container>
      <router-view></router-view>
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';
import { auth } from 'boot/firebase';

const router = useRouter();

const logout = () => {
  auth.signOut().then(() => {
    router.push('/login');
  });
};
</script>
