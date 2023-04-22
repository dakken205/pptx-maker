<template>
  <div>
    <q-layout view="hHh Lpr lff" container style="height: 100vh" class="">
      <q-header elevated :class="$q.dark.isActive ? 'bg-secondary' : 'bg-black'">
        <q-toolbar>
          <q-toolbar-title>DA研 定例会資料作成フォーム</q-toolbar-title>
          <q-btn flat @click="logout" round dense icon="logout" />
        </q-toolbar>
      </q-header>

      <q-drawer side="right" show-if-above bordered :width="150" :breakpoint="500"
        :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-3'">
        <div class="q-pa-sm">
          <div class="text-h6">
            <u>部門報告</u>
          </div>
          <template v-if="contentDialog.length !== 0">
            <div v-for="item, i in contentDialog" :key="i">
              <template v-if="i == 0">
                <div class="text-h6">
                  <u>連絡事項</u>
                </div>
              </template>
              <div class="text-subtitle1 q-ml-md">
                ・<u>{{ item.title }}</u>
              </div>
            </div>
          </template>
        </div>
      </q-drawer>

      <q-page-container>
        <q-page>
          <Content @update-dialog="handleDialog"></Content>
        </q-page>
      </q-page-container>
    </q-layout>
  </div>
</template>

<script>
import { ref } from 'vue'
import { getAuth, signOut, setPersistence, browserLocalPersistence } from 'firebase/auth'
import Content from '@/components/ContentForm.vue'

export default {
  components: {
    Content,
  },
  setup() {
    return {
      contentDialog: ref([]),
    }
  },
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
  },
  created() {
  },
  methods: {
    handleDialog(dialog) {
      this.contentDialog = dialog
    },
    logout() {
      signOut(this.$auth).then(() => {
        this.$router.push('/login')
      }).catch((err) => {
        console.log(err)
      })
    }
  },
  watch: {
    contentDialog(newVal) {
      this.contentDialog = newVal
    }
  }
}
</script>
