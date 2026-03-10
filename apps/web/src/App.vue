<template>
  <div id="app">

    <!-- NAVIGATION BAR PRO SELENIUM TEST -->
    <nav style="padding: 16px; background: #f0f0f0; margin-bottom: 16px;">
      <a href="/">Home</a>
    </nav>

    <!-- SEARCH BAR PRO SELENIUM TEST -->
    <input
      id="search"
      type="text"
      placeholder="Search..."
      style="padding: 8px; margin: 16px; width: 250px;"
    />

    <!-- OBSAH STRÁNKY -->
    <router-view />

    <!-- FOOTER PRO SELENIUM TEST -->
    <footer style="padding: 16px; background: #f0f0f0; margin-top: 32px;">
      <p>Footer content</p>
    </footer>

  </div>
</template>

<script setup>
// nic sem dávat nemusíš
</script>

<style>
/* tvoje styly */
</style>
