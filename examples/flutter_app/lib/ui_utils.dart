import 'package:flutter/material.dart';

Future<void> showCustomDialog(context, title, msg) {
  return showDialog(
    context: context,
    barrierDismissible: false, // user must tap button!
    builder: (BuildContext context) {
      return AlertDialog(
        title: Text(title),
        content: Text(msg),
        actions: [
          ElevatedButton(
            child: Text('OK'),
            onPressed: () {
              Navigator.of(context).pop();
            },
          ),
        ],
      );
    },
  );
}

void showCustomSnackBar(context, String msg) {
  ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(msg)));
}

Future<dynamic> showCustomRadioDialog(context, title, msg) {
  return showDialog(
    context: context,
    barrierDismissible: false, // user must tap button!
    builder: (BuildContext context) {
      int? selectedRadio = 0;
      return AlertDialog(
        title: Text(title),
        content: Column(
            mainAxisSize: MainAxisSize.min,
            children: [Text(msg),
              StatefulBuilder(
                  builder: (BuildContext context, StateSetter setState) {
                    return Column(
                        mainAxisSize: MainAxisSize.min,
                        children: List<Widget>.generate(4, (int index) {
                          return RadioListTile<int>(
                            title: Text('Radio ${index}'),
                            value: index,
                            groupValue: selectedRadio,
                            onChanged: (int? value) {
                              setState(() => selectedRadio = value);
                            },
                          );
                        }));
                  })
            ]),
        actions: [
          ElevatedButton(
            child: Text('OK'),
            onPressed: () {
              Navigator.of(context).pop(selectedRadio);
            },
          ),
        ],
      );
    },
  );
}