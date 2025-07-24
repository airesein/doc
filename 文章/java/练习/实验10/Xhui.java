import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Xhui {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("张三（123456）"); 
            frame.setSize(400, 300);
            frame.setLocationRelativeTo(null);

            JPanel mb = new JPanel();
            mb.setLayout(new BoxLayout(mb, BoxLayout.Y_AXIS));
            mb.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));

            JLabel bq = new JLabel("请选择语言");
            bq.setAlignmentX(Component.CENTER_ALIGNMENT);
            mb.add(bq);
            mb.add(Box.createVerticalStrut(10));

            JPanel button = new JPanel();
            button.setLayout(new FlowLayout());

            JButton chinese = new JButton("中文");
            button.add(chinese);

            JButton english = new JButton("English");
            button.add(english);

            mb.add(button);
            mb.add(Box.createVerticalStrut(10));

            JTextArea text = new JTextArea(10, 30);
            text.setEditable(false);
            text.setLineWrap(true);
            text.setWrapStyleWord(true);

            JScrollPane textmb = new JScrollPane(text);
            mb.add(textmb);

            frame.getContentPane().add(mb);

            chinese.addActionListener(new ActionListener() {
                public void actionPerformed(ActionEvent e) {
                    text.setText("你好，我是张三，学号为123456");
                }
            });

            english.addActionListener(new ActionListener() {
                public void actionPerformed(ActionEvent e) {
                    text.setText("Hello, I am Zhang San, and my student number is 123456");
                }
            });

            frame.setVisible(true);
        });
    }
}