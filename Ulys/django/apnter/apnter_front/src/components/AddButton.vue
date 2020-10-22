<template>
    <section>
        <router-link to="/new">
            <v-btn
            class="btn"
            fab
            color="cyan"
            top 
            right 
            fixed
            @click="add"
            >
            <v-icon>mdi-plus</v-icon>
            </v-btn>
        </router-link>
    </section>

</template>

<script>
export default {
    methods:{
        add(){

        }
    }
}
</script>

<style scoped>
    .btn{
        background-color: cyan;
    }
</style>