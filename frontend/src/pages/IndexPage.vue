<template>
  <q-drawer
    side="right"
    show-if-above
    bordered
    :width="150"
    :breakpoint="500"
    :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-3'"
  >
    <div class="q-pa-sm">
      <div class="text-h6">
        <u>部門報告</u>
      </div>
      <template v-if="contentDialog.length !== 0">
        <div v-for="(item, i) in contentDialog" :key="i">
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
  <q-layout>
    <q-page-container>
      <q-page>
        <Content @update-dialog="handleDialog"></Content>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import type { Dialog } from 'components/model';
import { ref } from 'vue';
import Content from 'components/ContentForm.vue';

const contentDialog = ref<Dialog[]>([]);

const handleDialog = (dialog: Dialog[]) => {
  contentDialog.value = dialog;
};
</script>
