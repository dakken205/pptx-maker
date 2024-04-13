<template>
  <q-card>
    <q-form>
      <div class="q-pa-md border">
        <div class="text-h5">定例会日時</div>
        <div class="q-pa-md">
          <div class="row" style="width: 100%">
            <q-input
              class="col-3"
              style="min-width: 150px"
              filled
              v-model="date"
              mask="date"
              :rules="['date']"
            >
              <template v-slot:append>
                <q-icon name="event" class="cursor-pointer">
                  <q-popup-proxy
                    cover
                    transition-show="scale"
                    transition-hide="scale"
                  >
                    <q-date
                      v-model="date"
                      :title="date"
                      subtitle="定例会開催日時"
                      :locale="{
                        months: [
                          '1月',
                          '2月',
                          '3月',
                          '4月',
                          '5月',
                          '6月',
                          '7月',
                          '8月',
                          '9月',
                          '10月',
                          '11月',
                          '12月',
                        ],
                        monthsShort: [
                          '1月',
                          '2月',
                          '3月',
                          '4月',
                          '5月',
                          '6月',
                          '7月',
                          '8月',
                          '9月',
                          '10月',
                          '11月',
                          '12月',
                        ],
                        days: [
                          '日曜日',
                          '月曜日',
                          '火曜日',
                          '水曜日',
                          '木曜日',
                          '金曜日',
                          '土曜日',
                        ],
                        daysShort: [
                          '日曜',
                          '月曜',
                          '火曜',
                          '水曜',
                          '木曜',
                          '金曜',
                          '土曜',
                        ],
                      }"
                    >
                      <div class="row items-center justify-end">
                        <q-btn
                          v-close-popup
                          label="Close"
                          color="primary"
                          flat
                        />
                      </div>
                    </q-date>
                  </q-popup-proxy>
                </q-icon>
              </template>
            </q-input>
            <div class="col q-gutter-x-sm" style="min-width: 130px">
              <q-btn
                @click="downloadPowerpoint"
                class="float-right"
                title="パワポのダウンロード"
                color="primary"
                icon="print"
              ></q-btn>
              <q-btn
                @click="save"
                class="float-right"
                title="下書き保存"
                color="primary"
                icon="save"
              ></q-btn>
              <q-btn
                @click="reset"
                class="float-right"
                title="記入内容リセット"
                color="red"
                icon="restart_alt"
              ></q-btn>
            </div>
          </div>
        </div>
      </div>
      <q-separator class="q-mt-xs"></q-separator>
      <div class="border q-mb-xs">
        <div class="text-h5 q-pa-md">部門報告</div>
        <div class="q-pa-md">
          <div class="row col-5 q-pb-sm">
            <div class="col-2">DS部門</div>
            <q-input
              :disable="!role.includes('ds')"
              v-model="ds"
              class="col-9"
              outlined
              dense
              autogrow
            ></q-input>
          </div>
          <div class="row col-5 q-pb-sm">
            <div class="col-2">DE部門</div>
            <q-input
              :disable="!role.includes('de')"
              v-model="de"
              class="col-9"
              outlined
              dense
              autogrow
            ></q-input>
          </div>
          <div class="row col-5 q-pb-sm">
            <div class="col-2">Biz部門</div>
            <q-input
              :disable="!role.includes('biz')"
              v-model="biz"
              class="col-9"
              outlined
              dense
              autogrow
            ></q-input>
          </div>
          <div class="row col-5 q-pb-sm">
            <div class="col-2">CC部門</div>
            <q-input
              :disable="!role.includes('cc')"
              v-model="cc"
              class="col-9"
              outlined
              dense
              autogrow
            ></q-input>
          </div>
        </div>
      </div>

      <q-list bordered>
        <div>
          <div class="text-h5 q-pa-md">連絡事項</div>
          <q-list>
            <q-card class="q-ml-md q-mr-md">
              <q-item class="border column" style="min-height: 170px">
                <div class="row col-5 q-pt-sm">
                  <div class="col-2">タイトル</div>
                  <q-input
                    v-model="pushingContent.title"
                    class="col-9"
                    outlined
                    dense
                  ></q-input>
                </div>
                <div class="row col q-pt-sm">
                  <div class="col-2">内容</div>
                  <q-input
                    v-model="pushingContent.content"
                    class="col-9"
                    dense
                    autogrow
                    outlined
                  ></q-input>
                  <!-- <q-input class="col-9" autogrow outlined ></q-input> -->
                </div>
                <div class="flex flex-center" style="width: 100%">
                  <q-btn
                    @click="addContent"
                    class="q-ma-sm float-center"
                    size="sm"
                    title="連絡事項の追加"
                    color="primary"
                    icon="add"
                    rounded
                  ></q-btn>
                </div>
              </q-item>
            </q-card>
            <template v-if="dialog.length === 0">
              <div
                style="
                  height: 100px;
                  width: 100%;
                  text-align: center;
                  padding-top: 30px;
                "
              >
                連絡事項未登録
              </div>
            </template>
            <q-item
              class="border column"
              v-for="(content, i) in dialog"
              :key="i"
              style="min-height: 170px"
            >
              <div class="row">
                <div class="col">
                  <div class="row col-5 q-pt-sm">
                    <div class="col-2">タイトル</div>
                    <q-field class="col-9" outlined dense>
                      <div
                        v-html="content.title"
                        class="text-black self-center full-width no-outline"
                      ></div>
                    </q-field>
                  </div>
                  <div class="row col q-pt-sm">
                    <div class="col-2">内容</div>
                    <q-field class="col-9" outlined dense>
                      <div
                        v-html="content.content"
                        class="text-black self-center full-width no-outline"
                      ></div>
                    </q-field>
                  </div>
                </div>
                <q-btn
                  @click="deleteInfoItem(i)"
                  class="col-1 q-mt-md"
                  icon="delete"
                  color="primary"
                  style="height: 50px"
                ></q-btn>
              </div>
            </q-item>
          </q-list>
        </div>
      </q-list>
    </q-form>
  </q-card>
</template>

<script setup lang="ts">
import type { Dialog } from './model';
import { ref, onBeforeMount, onMounted } from 'vue';
import { useQuasar } from 'quasar';
import { auth, firestore } from 'boot/firebase';
import { api } from 'boot/axios';
import { updateDoc, getDoc, doc, onSnapshot } from 'firebase/firestore';
import dayjs from 'dayjs';
import 'dayjs/locale/ja';
import { browserLocalPersistence } from 'firebase/auth';

dayjs.locale('ja');

const today = dayjs(new Date()).format('YYYY/MM/DD');

const $q = useQuasar();

onBeforeMount(() => {
  onSnapshot(doc(firestore, '/root/departments'), (docSnapshot) => {
    const data = docSnapshot.data();
    if (!data) return;

    ds.value = data.ds;
    de.value = data.de;
    biz.value = data.biz;
    cc.value = data.cc;
    dialog.value = data.info_contents as Dialog[];
    dialog.value = [...dialog.value, ...myNewDialog.value];
  });
});

onMounted(() => {
  auth.setPersistence(browserLocalPersistence).then(() => {
    if (!auth.currentUser) return;
    getDoc(doc(firestore, `users/${auth.currentUser.email}`)).then(
      (docSnapshot) => {
        if (!docSnapshot.exists()) return;
        role.value = docSnapshot.data().role;
      }
    );
  });
});

const date = ref(today);
const ds = ref('');
const de = ref('');
const biz = ref('');
const cc = ref('');
const initialContent = {
  title: '',
  content: '',
};
const pushingContent = ref<Dialog>({
  title: '',
  content: '',
});
const myNewDialog = ref<Dialog[]>([]);
const role = ref('');
const dialog = ref<Dialog[]>([]);

const showLoading = (message: string) => {
  $q.loading.show({
    message: message,
  });
};

const hideLoading = () => {
  $q.loading.hide();
};

const addContent = () => {
  const pushItem = JSON.parse(JSON.stringify(pushingContent.value));
  const dialogItem = JSON.parse(JSON.stringify(pushItem));
  const newDialog = JSON.parse(JSON.stringify(dialog.value));
  newDialog.push(dialogItem);

  dialog.value = newDialog;
  myNewDialog.value.push(pushItem);
  pushingContent.value = initialContent;
};

const save = async () => {
  showLoading('Database operations are in progress. Hang on...');
  myNewDialog.value = [];
  const data = {
    ds: ds.value,
    de: de.value,
    biz: biz.value,
    cc: cc.value,
    info_contents: dialog.value,
  };
  try {
    await updateDoc(doc(firestore, '/root/departments'), data);
    $q.notify({
      message: '下書き保存しました',
      color: 'positive',
      position: 'top',
      timeout: 2000,
    });
  } catch {
    $q.notify({
      message: '下書き保存に失敗しました',
      color: 'negative',
      position: 'top',
      timeout: 2000,
    });
  } finally {
    hideLoading();
  }
};

const downloadPowerpoint = () => {
  const datefmt = dayjs(date.value).format('YYYY年MM月DD日（ddd）');
  const datefmt_filename = dayjs(date.value).format('YYYYMMDD');
  const info_contents = dialog;
  const departments_contents = {
    ds: ds.value,
    de: de.value,
    biz: biz.value,
    cc: cc.value,
  };
  const params = {
    departments_contents: departments_contents,
    datefmt: datefmt,
    datefmt_filename: datefmt_filename,
    info_contents: info_contents.value,
  };
  api.post('/generate', params).then((res) => {
    // Note data.file is a base64 string of pptx file
    // TODO: atob may be deprecated
    const fileContent = atob(res.data.file);

    // Convert the base64 string to a byte array
    let byteArray = new Uint8Array(fileContent.length);
    for (let i = 0; i < fileContent.length; i++) {
      byteArray[i] = fileContent.charCodeAt(i);
    }

    // Create a Blob object from the byte array
    const blob = new Blob([byteArray], {
      type: 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
    });
    const url = window.URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', res.data.filename);
    document.body.appendChild(link);
    link.click();
  });
};

const reset = () => {
  ds.value = '';
  de.value = '';
  biz.value = '';
  cc.value = '';
  pushingContent.value = initialContent;
  dialog.value = [];
};

const deleteInfoItem = (i: number) => {
  dialog.value.splice(i, 1);
};
</script>
