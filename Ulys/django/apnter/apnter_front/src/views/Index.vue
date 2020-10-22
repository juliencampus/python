<template>
    <section>
        <vue-cal style = "height: 880px" 
                :events = "events"
                :time-from = "9 * 60"
                :time-to = "18 * 60"
                :time-cell-height="100"
                hide-weekends/>
    </section>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import VueCal from 'vue-cal'
import 'vue-cal/dist/vuecal.css'
export default {
    components: {
        VueCal
    },
    data: () => ({
        someVar: 'oui',
    }),
    created(){
        this.getAppointments()
    },
    computed: {
        ...mapState(['appointments']),
        events(){
            return this.appointments.map(obj => ({
            start: new Date(Date.parse(obj.starts_at)),
            end: new Date(Date.parse(obj.ends_at)),
            title: obj.patient,
            class: obj.duration == "1800.0" ? "simple" : obj.duration == "2700.0" ? "spe" : "handle"
            }))
        }
    },
    methods: {
        ...mapActions(['getAppointments'])
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