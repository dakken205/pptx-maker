<template>
    <q-card>
        <q-form>
            <div class="q-pa-md border">
                <div class="text-h5">定例会日時</div>
                <div class="q-pa-md">
                    <div class="row" style="width: 100%;">
                        <q-input class="col-3" style="min-width: 150px;" filled v-model="date" mask="date"
                            :rules="['date']">
                            <template v-slot:append>
                                <q-icon name="event" class="cursor-pointer">
                                    <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                                        <q-date v-model="date" :title="date" subtitle="定例会開催日時" :locale="{
                                                months: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
                                                monthsShort: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
                                                days: ['日曜日', '月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日'],
                                                daysShort: ['日曜', '月曜', '火曜', '水曜', '木曜', '金曜', '土曜']
                                            }">
                                            <div class="row items-center justify-end">
                                                <q-btn v-close-popup label="Close" color="primary" flat />
                                            </div>
                                        </q-date>
                                    </q-popup-proxy>
                                </q-icon>
                            </template>
                        </q-input>
                        <div class="col q-gutter-x-sm" style="min-width: 130px;">
                            <q-btn @click="donwloadPowerpoint" class="float-right" title="パワポのダウンロード" color="primary"
                                icon="print"></q-btn>
                            <q-btn @click="save" class="float-right" title="下書き保存" color="primary" icon="save"></q-btn>
                            <q-btn @click="reset" class="float-right" title="記入内容リセット" color="red"
                                icon="restart_alt"></q-btn>
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
                        <q-input v-model="ds" class="col-9" outlined dense autogrow></q-input>
                    </div>
                    <div class="row col-5 q-pb-sm">
                        <div class="col-2">DE部門</div>
                        <q-input v-model="de" class="col-9" outlined dense autogrow></q-input>
                    </div>
                    <div class="row col-5 q-pb-sm">
                        <div class="col-2">Biz部門</div>
                        <q-input v-model="biz" class="col-9" outlined dense autogrow></q-input>
                    </div>
                    <div class="row col-5 q-pb-sm">
                        <div class="col-2">CC部門</div>
                        <q-input v-model="cc" class="col-9" outlined dense autogrow></q-input>
                    </div>
                </div>
            </div>

            <q-list bordered>
                <div>
                    <div class="text-h5 q-pa-md">連絡事項</div>
                    <q-list>
                        <q-card class="q-ml-md q-mr-md">
                            <q-item class="border column" style="min-height: 170px;">
                                <div class="row col-5 q-pt-sm">
                                    <div class="col-2">タイトル</div>
                                    <q-input v-model="pushingContent.title" class="col-9" outlined dense></q-input>
                                </div>
                                <div class="row col q-pt-sm">
                                    <div class="col-2">内容</div>
                                    <q-input v-model="pushingContent.content" class="col-9" dense autogrow
                                        outlined></q-input>
                                    <!-- <q-input class="col-9" autogrow outlined ></q-input> -->
                                </div>
                                <div class="flex flex-center" style="width: 100%;">
                                    <q-btn @click="addContent" class="q-ma-sm float-center" size="sm" title="連絡事項の追加"
                                        color="primary" icon="add" rounded></q-btn>
                                </div>
                            </q-item>
                        </q-card>
                        <template v-if="dialog.length === 0">
                            <div style="height: 100px; width: 100%; text-align: center; padding-top: 30px;">連絡事項未登録</div>
                        </template>
                        <q-item class="border column" v-for="content, i in dialog" :key="i" style="min-height: 170px;">
                            <div class="row">
                                <div class="col">
                                    <div class="row col-5 q-pt-sm">
                                        <div class="col-2">タイトル</div>
                                        <q-field class="col-9" outlined dense>
                                            <div v-html="content.title"
                                                class="text-black self-center full-width no-outline">
                                            </div>
                                        </q-field>
                                    </div>
                                    <div class="row col q-pt-sm">
                                        <div class="col-2">内容</div>
                                        <q-field class="col-9" outlined dense>
                                            <div v-html="content.content"
                                                class="text-black self-center full-width no-outline">
                                            </div>
                                        </q-field>
                                    </div>
                                </div>
                                <q-btn @click="deleteInfoItem(i)" class="col-1 q-mt-md" icon="delete" color="primary"
                                    style="height: 50px;"></q-btn>
                            </div>
                        </q-item>
                    </q-list>
                </div>

            </q-list>
        </q-form>
    </q-card>
</template>

<script>
import { ref } from 'vue'
import { updateDoc, getDoc, doc, onSnapshot } from 'firebase/firestore'

import dayjs from 'dayjs'
import 'dayjs/locale/ja'
dayjs.locale('ja')

const today = dayjs(new Date()).format('YYYY/MM/DD')
const initialContent = {
    title: '',
    content: '',
}
let info_contents_listener = null
console.log(info_contents_listener)

export default {
    setup() {
        return {
            date: ref(today),
            ds: ref(''),
            de: ref(''),
            biz: ref(''),
            cc: ref(''),
            pushingContent: ref({
                title: '',
                content: '',
            }),
            dialog: ref([]),
        }
    },
    beforeCreate() {
        onSnapshot(doc(this.$firestore, '/root/departments'), docSnapshot => {
            this.ds = docSnapshot.data().ds
            this.de = docSnapshot.data().de
            this.biz = docSnapshot.data().biz
            this.cc = docSnapshot.data().cc
            this.contents = docSnapshot.data().info_contents
            this.dialog = docSnapshot.data().info_contents
        })
    },
    async created() {
        getDoc(doc(this.$firestore, '/root/departments'))
            .then(docSnapshot => {
                this.ds = docSnapshot.data().ds
                this.de = docSnapshot.data().de
                this.biz = docSnapshot.data().biz
                this.cc = docSnapshot.data().cc
                this.contents = docSnapshot.data().info_contents
                this.dialog = docSnapshot.data().info_contents
            })
    },
    methods: {
        addContent() {
            const pushItem = JSON.parse(JSON.stringify(this.pushingContent))
            let dialogItem = JSON.parse(JSON.stringify(pushItem))
            let newDialog = JSON.parse(JSON.stringify(this.dialog))
            newDialog.push(dialogItem)
            this.dialog = newDialog

            this.pushingContent = initialContent
        },

        save() {
            const data = {
                ds: this.ds,
                de: this.de,
                biz: this.biz,
                cc: this.cc,
                info_contents: this.dialog,
            }
            updateDoc(doc(this.$firestore, '/root/departments'), data)
        },
        donwloadPowerpoint() {
            const datefmt = dayjs(this.date).format('YYYY年MM月DD日（ddd）')
            const datefmt_filename = dayjs(this.date).format('YYYYMMDD')
            const info_contents = this.dialog
            const departments_contents = {
                ds: [this.ds],
                de: [this.de],
                biz: [this.biz],
                cc: [this.cc],
            }
            // const info_contents = {

            // }
            const params = {
                departments_contents: departments_contents,
                datefmt: datefmt,
                info_contents: info_contents,
            }
            this.$axios.post('/generate', params).then(function (response) {
                const downloadURL = response.data.download_url
                const downloadLink = document.createElement('a')
                downloadLink.href = downloadURL
                downloadLink.download = `${datefmt_filename}.pptx`
                downloadLink.click()
            }.bind(this))
        },
        htmlText(msg) {
            if (msg instanceof String) {
                return msg.replace('\r\n', '<br>')
            }
        },
        reset() {
            this.ds = ''
            this.de = ''
            this.biz = ''
            this.cc = ''
            this.contents = []
            this.pushingContent = initialContent
            this.dialog = []
        },
        deleteInfoItem(i) {
            this.dialog = this.contents.splice(i, 1)
        }
    },
    watch: {
        dialog(newVal) {
            this.$emit('update-dialog', newVal)
        }
    }
}

</script>