<template>
    <section>
        <h1>Oui</h1>
        <!-- <VueCal style="height:300px"/> -->
    </section>
</template>

<script>
import { mapActions, mapState } from 'vuex'
// import VueCal from 'vue-cal'
import 'vue-cal/dist/vuecal.css'
export default {
    components: {
        // VueCal
    },
    data: () => ({

    }),
    created(){
        this.getAppointments()
    },
    computed: {
        ...mapState(['appointments'])
    },
    methods: {
        ...mapActions(['getAppointments'])
    }
}
</script>

<style scoped>

</style>