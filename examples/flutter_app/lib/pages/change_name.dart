import 'package:flutter/material.dart';
import 'package:flutter_app/ui_utils.dart';
import 'package:provider/provider.dart';
import 'package:flutter_app/app_state.dart';

class _ScaffoldBody extends StatelessWidget {
  final TextEditingController textEditingController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    textEditingController.text = Provider.of<AppState>(context).currentUser;
    var appState = Provider.of<AppState>(context);

    return Column(children: [
      Row(children: [
        Text('Name: '),
        Expanded(child: TextField(controller: textEditingController)),
      ]),
      ElevatedButton(
          child: Text("Change"),
          onPressed: () {
            if (textEditingController.text.isEmpty) {
              showCustomSnackBar(context, "Empty Name!");
              return;
            }
            appState.currentUser = textEditingController.text;
            Navigator.pop(context);
          })
    ]);
  }
}

class ChangeNamePage extends StatelessWidget {
  static const nav_url = '/change_name';
  static const menu_name = 'Change Name';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(title: Text(menu_name)), body: _ScaffoldBody());
  }
}
