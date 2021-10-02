package com.example.repository_pattern

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.TextView
import androidx.lifecycle.ViewModelProvider
import java.lang.StringBuilder

// The repository pattern is a strategy for abstracting data access.
// ViewModel delegates the data-fetching process to the repository.

class MainActivity : AppCompatActivity() {
    private lateinit var myViewModel : MyViewModel

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        myViewModel = ViewModelProvider(this, MyViewModel.Factory(this)).get(MyViewModel::class.java)

        myViewModel.repos.observe(this) { repos ->
            val response = StringBuilder().apply {
                repos.forEach {
                    append(it.name)
                    append(" - ")
                    append(it.owner)
                    append("\n")
                }
            }.toString()
            findViewById<TextView>(R.id.textResponse).text = response
        }
    }
}