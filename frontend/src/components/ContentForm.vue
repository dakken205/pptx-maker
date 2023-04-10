<template>
    <q-form>
        <div class="q-pa-sm border">
            <div class="text-h5">定例会日時</div>
            <div class="q-pa-md">
                <div class="row" style="width: 100%;">
                    <q-input class="col-3" style="min-width: 150px;" filled v-model="date" mask="date" :rules="['date']">
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
                    </div>
                </div>
            </div>
        </div>
        <q-separator class="q-mt-xs"></q-separator>
        <div class="border q-mb-xs">
            <div class="text-h5 q-pa-sm">部門報告</div>
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
                <div class="text-h5 q-pa-sm">連絡事項</div>
                <q-list>
                    <q-item class="border column" style="min-height: 170px;">
                        <div class="row col-5 q-pt-sm">
                            <div class="col-2">タイトル</div>
                            <q-input v-model="pushingContent.title" class="col-9" outlined dense></q-input>
                        </div>
                        <div class="row col q-pt-sm">
                            <div class="col-2">内容</div>
                            <q-input v-model="pushingContent.content" class="col-9" dense autogrow outlined></q-input>
                            <!-- <q-input class="col-9" autogrow outlined ></q-input> -->
                        </div>
                        <div class="flex flex-center" style="width: 100%;">
                            <q-btn @click="addContent" class="q-ma-sm float-center" size="sm" title="連絡事項の追加" color="black"
                                icon="add" rounded></q-btn>
                        </div>
                    </q-item>
                    <q-item class="border column" v-for="content, i in contents" :key="i" style="min-height: 170px;">
                        <div class="row col-5 q-pt-sm">
                            <div class="col-2">タイトル</div>
                            <q-field class="col-9" outlined dense>
                                <div v-html="content.title" class="self-center full-width no-outline"></div>
                            </q-field>
                        </div>
                        <div class="row col q-pt-sm">
                            <div class="col-2">内容</div>
                            <q-field class="col-9" outlined dense>
                                <div v-html="content.content" class="self-center full-width no-outline"></div>
                            </q-field>
                        </div>
                    </q-item>
                </q-list>
            </div>

        </q-list>
    </q-form>
</template>

<script>
import { ref } from 'vue'

import dayjs from 'dayjs'
import 'dayjs/locale/ja'
dayjs.locale('ja')

const today = dayjs(new Date()).format('YYYY/MM/DD')
const initialContent = {
    title: '',
    content: '',
}

export default {
    setup() {
        return {
            date: ref(today),
            ds: ref(''),
            de: ref(''),
            biz: ref(''),
            cc: ref(''),
            contents: ref([]),
            pushingContent: ref({
                title: '',
                content: '',
            })
        }
    },
    created() {
        console.log(this.date)
    },
    methods: {
        addContent() {
            const pushItem = JSON.parse(JSON.stringify(this.pushingContent))
            console.log(pushItem)
            console.log(this.htmlText(pushItem.content))
            this.contents.push(pushItem)
            this.pushingContent = initialContent
        },
        save() {
            console.log(this.ds)
            console.log(this.de)
            console.log(this.biz)
            console.log(this.cc)
        },
        donwloadPowerpoint() {
            console.log(this.ds)
            console.log(this.de)
            console.log(this.biz)
            console.log(this.cc)
        },
        htmlText(msg) {
            if (msg instanceof String) {
                return msg.replace('\r\n', '<br>')
            }
        },
    },
    watch: {

    }
}

</script>