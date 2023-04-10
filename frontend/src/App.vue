<template>
  <div>
    <q-layout view="hHh Lpr lff" container style="height: 100vh" class="">
      <q-header elevated :class="$q.dark.isActive ? 'bg-secondary' : 'bg-black'">
        <q-toolbar>
          <!-- <q-btn flat @click="drawerLeft = !drawerLeft" round dense icon="menu" /> -->
          <q-toolbar-title>DA研 定例会資料作成フォーム</q-toolbar-title>
          <q-btn flat @click="drawerRight = !drawerRight" round dense icon="menu" />
        </q-toolbar>
      </q-header>

      <!-- <q-drawer
        v-model="drawerLeft"
        show-if-above
        :width="250"
        :breakpoint="700"
        elevated
        class="bg-white text-black"
      >
      <div class="text-h5 q-pa-md border" style="height: 60px;">
        定例会資料のログ
      </div>
        <q-scroll-area style="height: calc(100vh - 110px);">
            <q-list bordered>
              <q-item class="border" clickable v-ripple v-for="n in 20" :key="n">
                <q-item-section>
                  {{ n }}
                </q-item-section>
              </q-item>
            </q-list>
        </q-scroll-area>
      </q-drawer> -->

      <q-drawer
        side="right"
        v-model="drawerRight"
        show-if-above
        bordered
        :width="150"
        :breakpoint="500"
        :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-3'"
      >
        <q-scroll-area class="fit">
          <div class="q-pa-sm">
            <div v-for="n in 50" :key="n">Drawer {{ n }} / 50</div>
          </div>
        </q-scroll-area>
      </q-drawer>

      <q-page-container>
        <q-page>
          <Content></Content>
        </q-page>
      </q-page-container>
    </q-layout>
  </div>
</template>

<script>
import { ref } from 'vue'
import Content from '@/components/ContentForm.vue'

export default {
  components: {
    Content,
  },
  setup () {
    return {
      drawerLeft: ref(false),
      drawerRight: ref(false)
    }
  }
}
</script>

<style>
.border {
  border-bottom: solid 1px rgb(219, 219, 219);
}
</style>