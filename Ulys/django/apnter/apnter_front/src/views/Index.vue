<template>
    <section>
        <v-btn v-if="!show" type="button" @click="updateComponent" >show</v-btn>
        <AddButton v-if="show"/>
        <vue-cal style = "height: 880px" 
                :events = "events"
                :time-from = "9 * 60"
                :time-to = "18 * 60"
                :time-cell-height="100"
                hide-weekends
                v-if="show"
                :on-event-click="onEventclick"
                />
    </section>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import VueCal from 'vue-cal'
import 'vue-cal/dist/vuecal.css'
import AddButton from '@/components/AddButton'     

export default {
    components: {
        VueCal,
        AddButton
    },
    created(){
        this.getAppointments()
        const socket = new WebSocket('ws://127.0.0.1:8000')
        socket.onopen =  () =>{
            socket.send('listener', true)
            socket.send('appointment', '123')
        }
        socket.onmessage = (data) => {
            console.log(data)
            this.$store.commit('setAppointments', data)
        }
    },
    data: () => ({
        show: false
    }),
    computed: {
        ...mapState(['appointments']),

        events(){
            let aptns_from_api = this.appointments.map(obj => ({
            start: new Date(Date.parse(obj.starts_at)),
            end: new Date(Date.parse(obj.ends_at)),
            title: obj.patient,
            class: obj.duration == "1800.0" ? "simple" : obj.duration == "2700.0" ? "spe" : "handle"
            }))
            return aptns_from_api
        }

    },
    methods: {
        ...mapActions(['getAppointments']),
        updateComponent(){
            this.show = true
        },
        onEventclick(event,e ){
            console.log(event)
            console.log(e)
        }
    }
}
</script>

<style>
    .vuecal__event.simple {
        background-color: rgba(164, 230, 210, 0.9)
    }
    .vuecal__event.spe {
        background-color: rgba(223, 116, 217, 0.9)
    }
    .vuecal__event.handle {
        background-color: rgba(223, 179, 85, 0.9)
    }
    .vuecal__event{
        padding : 5px
    }
</style>